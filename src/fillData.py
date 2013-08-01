from fakeInfo import FakeData
import random, time
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support import expected_conditions as EC

#Used to fill out forms
class Filler(object):

  fake_info = None
  program_url = None

  def __init__(self, url):
    self.fake_info = FakeData()
    self.program_url = url

  def create_random_username(self):
    self.fake_info.create_random_username()

  def _fill_text_box(self, element, page=None):
    
    print element.tag_name, element.get_attribute('id'), "sending keys"
    if element.is_displayed()==True:
      if 'autocomplete' in element.get_attribute('class'):
        k = Keys()
        #temp value: 'Mar' is temporarily being used because it is triggering the autocomplete dropdown for the three autocomplete textboxes
        element.send_keys('Mar')
      
        element.send_keys(k.ARROW_DOWN)
        
        #wait_element = page.wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'autocomplete')]")))
        wait_element = page.ip.is_element_clickable_by_xpath("//li[contains(@class, 'autocomplete')]")

        highlighted_element = page.driver.find_element_by_xpath("//li[contains(@class, 'autocomplete')]")
        highlighted_element.click()
      else:
        element.clear()
        info = self.fake_info.fill_valid_value(element)
        element.send_keys(info)
  
  #selects the first option from a combo box
  def _select_combo(self, element, option):
    print element.get_attribute('id'), 'selecting'
    select = Select(element)
    select.select_by_index(option)

  def _click_radio(self, element, fieldset):
    print 'radio button'

    #finds all html children of a fieldset tag
    for sub_tag in fieldset.find_elements_by_xpath("*"):  
      #iterates through child nodes until it finds the ol child
      #the ol child would carry information about whether or not the radio button is linked to hidden data fields
      if sub_tag.tag_name=='ol':
        #for radio buttons where a 'yes' would expand a hidden node, the words 'if' or 'location' are used in the ol class attribute
        if 'if' in sub_tag.get_attribute('class') or 'location' in sub_tag.get_attribute('class'):
          #since 'if' is in the class attribute field we want to find and click the 'yes' radio button
          if 'yes' in element.get_attribute('id'):
            print 'clicking: '+element.get_attribute('id'), 'yes'
            element.click()
        #for radio buttons where a 'no' would expand a hidden node, the word 'not' is used in the ol class attribute
        elif 'not' in sub_tag.get_attribute('class'):
          #since 'not' is in the class attribute field we want to find and click the 'no' radio button
          if 'no' in element.get_attribute('id'):
            print 'clicking: '+element.get_attribute('id'), 'no'
            element.click()
      else:
        if '.female' in element.get_attribute('id'):
          element.click() #by default selects female radio button
        elif '.yes' in element.get_attribute('id'):
          element.click() #by default selects 'yes' radio button
        '''try:
          #randomly choose an option for gender
          gender_inputs = fieldset.find_elements_by_xpath(".//input[contains(@id, 'gender')]")
          random_number = random.choice(range(0,2))
          print gender_inputs[random_number].get_attribute('id')
          gender_inputs[random_number].click()
          break
        except Exception, e:
          pass'''

  def _attach_a_file(self, element, fieldset, page):    
    element = self._check_before_upload(element, fieldset, page)

    print '**********'
    print 'Attaching file:', 'test_doc'
    
    #path to 
    print 'path to file:', self.fake_info.path_to_test_doc
    #gives file path to input element
    try:
      element.send_keys(self.fake_info.path_to_test_doc)
    except Exception, e:
      print 'upload failed'
      print 'trying again'
      element = fieldset.find_element_by_xpath(".//input[@type='file']")
      element.send_keys(self.fake_info.path_to_test_doc)
    
    self._wait_for_upload_to_complete(element, fieldset)
    
    print 'Upload Complete'

  def _click_checkbox(self, element):
    checkbox = element
    if checkbox.is_selected()==False:
      print 'checkbox', checkbox.get_attribute('value')
      checkbox.click()

  def _wait_for_upload_to_complete(self, element, fieldset):
    button_name = ''
    while 'test_doc' not in button_name:
      try:
        button_name = fieldset.find_element_by_xpath(".//a[@class='button']").text
      except Exception, e:
        pass

  def _check_before_upload(self, element, fieldset, page):
    upload_button = fieldset.find_element_by_xpath(".//a[@class='button']")
    upload_button_text = upload_button.text
    if 'test_doc' in upload_button_text:
      delete_button = upload_button.find_element_by_xpath(".//span[contains(@class, 'delete')]")
      delete_button.click()
      alert = page.driver.switch_to_alert()
      alert.accept()
      print '**********'
      print 'previous upload deleted'
      element_after_file_deletion = fieldset.find_element_by_xpath(".//input[@type='file']")
      return element_after_file_deletion
    else:
      return element                

  def _fill_text_area(self, element): #not tested yet
    print element.tag_name, element.get_attribute('id'), "sending keys"
    if element.is_displayed()==True:
      element.clear()
      element.send_keys(self.fake_info.lorem())

  #handles section tags that contain inline in the id
  def _inline_section(self, element, page):
    print 'adding'
    add_button = element.find_element_by_xpath(".//a[contains(@class, 'button action medium add')]")
    save_button = element.find_element_by_xpath(".//a[contains(@class, 'button medium action save')]")
  
    #clicks add button for an inline section
    add_button.click()
   
    #finds input, select and fieldset tags for the newly expanded inline section    
    sub_tr = element.find_element_by_xpath(".//tr[@class='editing']")
    inputs = sub_tr.find_elements_by_xpath(".//select[@id!='']|.//input[@id!='']")
    inputs_file = sub_tr.find_elements_by_xpath(".//input[@type='file']")
    fieldset = sub_tr.find_element_by_xpath(".//fieldset")
    
    self._sort_and_fill(inputs, fieldset, page)
    self._sort_and_fill(inputs_file, sub_tr)

    #saves info after filling in section
    save_button.click()
    
    print '**********'
    print 'saving'

    wait_element = page.ip.is_element_visible(add_button)
    #wait_element = page.ip.is_element_clickable_by_xpath(".//a[contains(@class, 'button medium action save')]")

  def _sort_and_fill(self, inputs, fieldset=None, page=None):
    index = 0

    while index < len(inputs):
      field = inputs[index]
      print '*********'
      #handles state field in a special manner because the state field switches from a text box
      #to a combo box if the US is selected as the country
      if 'location' in field.get_attribute('id'):
        #refinds the state field because it changes from a text box to a combo box depending on the country selected
        state_field = fieldset.find_element_by_xpath(".//select[contains(@id, 'state')]")
        self._select_combo(state_field, 1)
      
      #checks to see if a text field is visible then sends keys.
      elif field.get_attribute('type')=='text' or field.get_attribute('type')=='email' and field.is_displayed()==True:
        self._fill_text_box(field, page=page)

      #selects yes or no depending on whether button triggers a node to expand
      elif field.get_attribute('type')=='radio':
        self._click_radio(field, fieldset)
        
      #selects the first option in combo boxes
      elif field.tag_name=='select':
        self._select_combo(field, 1)

      elif field.get_attribute('type')=='file':
        self._attach_a_file(field, fieldset, page)

      elif field.get_attribute('type')=='checkbox':
        self._click_checkbox(field)

      elif field.tag_name=='textarea':
        self._fill_text_area(field)
        
      index += 1 

  #takes in a page and fills in text boxes, clicks radio buttons, uploads files, and selects from combo boxes 
  def auto_fill(self, page):
    #temporary. wait for page to load.
    time.sleep(2)
    '''try:
      header = page.driver.find_element_by_xpath("//h3[contains(text(), '"+page.name+"')]")
      wait_element = page.ip.is_element_visible(header)
    except Exception, e:
      page.navigate_to()
      time.sleep(2)'''

    #this is a list
    #grabs anything with either a fieldset tag or section tag contiaining the word 'inline' in its id field
    fieldsets_inlines = page.driver.find_elements_by_xpath("//fieldset|//section[contains(@id, 'inline')]")

    print '***start***'

    #iterates through fieldsets_inlines list and for each fieldset/section tag, finds the input
    #and/or select elements, then interacts with them appropriately
    for tag in fieldsets_inlines:
      #only evaluates elements on current page
      if tag.is_displayed()==True:
        if tag.tag_name=='fieldset':
          #look for select, textarea and input tags where id is not the null string
          #also looks for input tags where type is 'file'
          inputs = tag.find_elements_by_xpath(".//select[@id!='']|.//input[@id!='']|.//input[@type='file']|.//input[@type='checkbox']|.//textarea[@id!='']")
          #calls _sort_and_fill() method using input/select element and the fieldset tag of its ancestral node 
          self._sort_and_fill(inputs, tag, page)
        elif tag.tag_name=='section':
          self._inline_section(tag, page)
    
    print '***end***'