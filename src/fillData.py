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

  #fills out current page. use after navigating to desired page.
  def auto_fill(self, page):
    time.sleep(3) #short wait just in case page need a while to load.
    print '***START***'
    #grabs relevant section tags
    all_sections = page.driver.find_elements_by_xpath("//section[contains(@id, 'section')]|//section[@class='application preview']")
    for section in all_sections:
      if section.is_displayed()==True: #iterate through list and if current page is highlighted in html then method continues
        print section.get_attribute('id')
        #gets form tags and section tags with 'inline' in id attribute
        forms_and_inline_sections = section.find_elements_by_xpath(".//form|.//section[contains(@id, 'inline')]")
        for tag in forms_and_inline_sections:
          print tag.get_attribute('id')
          if tag.tag_name=='form':
            form = tag
            if 'form' in form.get_attribute('id'):
              self._to_fieldsets(page, form) #parses form tag into fieldset tags before filling out individual data fields
            else:
              self._to_all_data_fields(page, form) #used as alternate way of uploading files
          elif tag.tag_name=='section':
            inline_section = tag
            self._inline_section(page, inline_section) #inline sections need to be handled in a special manner
        break
      elif section.get_attribute('class')=='application preview': #special case for preview page
        print section.get_attribute('class')
        form_tags = section.find_elements_by_tag_name('form')
        for form in form_tags:
          self._to_fieldsets(page, form)
        break
    
    print '***END***'

  def auto_fill_iframe(self, page): #used for payment window
    time.sleep(3)
    print '***START***'
    payment_form = page.driver.find_element_by_tag_name('form')
    self._to_fieldsets(page, payment_form)

    print '***END***'

  def _to_fieldsets(self, page, form): #parse form tag into fieldset tags
    fieldsets = form.find_elements_by_tag_name("fieldset") #finds fieldset tag children of given form tag
    for fieldset_tag in fieldsets:
      if 'practice_law' not in fieldset_tag.get_attribute('class'): #special condition to skip a particular form in wu-llm program
        all_data_fields = fieldset_tag.find_elements_by_xpath(".//select|.//input|.//textarea") #grabs webelements/data fields that are children of given fieldset tag
        for data_field in all_data_fields:
          if data_field.is_displayed()==True or 'location' in data_field.get_attribute('id'): #checks to see if webelement is visible so as to prevent an exception from being thrown
            self._fill(data_field, fieldset_tag, page) #sends each webelement/data field to get sorted and filled with appropriate data

  def _to_all_data_fields(self, page, form):
    all_data_fields = form.find_elements_by_xpath(".//input") #used specifically an alternate way to upload files
    for data_field in all_data_fields:
      if data_field.get_attribute('type')=='file':
        try:
          tags = data_field.find_elements_by_xpath("ancestor::div[contains(@class, 'supload') and not(contains(@class, 'complete') and not(contains(@class, 'mask'))]")
          for div_tag in tags:
            if div_tag.is_displayed()==True:
              self._fill(data_field, div_tag, page)
              break
        except Exception, e:
          tags = data_field.find_elements_by_xpath("ancestor::div[contains(@class, 'supload') and not(contains(@class, 'mask'))]")
          for div_tag in tags:
            if div_tag.is_displayed()==True:
              self._fill(data_field, div_tag, page)
              break

  def _fill(self, data_field, tag, page):
    if 'location' in data_field.get_attribute('id'): #handles state field in a special manner because the state field switches from a text box to a combo box if the US is selected as the country
      state_field = tag.find_element_by_xpath(".//select[contains(@id, 'state')]") #refinds the state field because it changes from a text box to a combo box depending on the country selected
      self._select_combo(state_field, 1)
    
    elif data_field.get_attribute('type')=='text' or data_field.get_attribute('type')=='email':
      self._fill_text_box(data_field, page)
      
    elif data_field.get_attribute('type')=='radio':
      #in this case, tag == fieldset_tag
      self._click_radio(data_field, tag) #selects yes or no depending on whether button triggers a node to expand
      
    elif data_field.get_attribute('type')=='file':
      #in this case, tag == div
      self._attach_a_file(data_field, tag, page)

    elif data_field.tag_name=='select':
      self._select_combo(data_field, 1) #selects the first option in combo boxes

    elif data_field.get_attribute('type')=='checkbox':
      self._click_checkbox(data_field)

    elif data_field.tag_name=='textarea':
      self._fill_text_area(data_field)

  def _click_radio(self, data_field, fieldset_tag): 
    data_field_id = data_field.get_attribute('id')

    if 'yes' in data_field_id or 'no' in data_field_id: 
      try:
        if 'not_applicable' in data_field_id: #special condition for visa status question in ___ program
          print 'clicking: ', data_field_id
          data_field.click()
        else:
          self._yes_no_radio_button(fieldset_tag, data_field)
      except Exception, e:
        if 'yes' in data_field_id:
          print 'clicking: ', data_field_id
          data_field.click()
    else:
      self._miscellaneous_radio_button(data_field)
    # elif 'gender' in data_field_id:
    #   if 'female' in data_field_id:
    #     print 'clicking: ', data_field_id
    #     data_field.click()
    # elif 'score_type' in data_field_id:
    #   if 'manual' in data_field_id:
    #     data_field.click()
    # elif 'marital_status' in data_field_id:
    #   if 'single' in data_field_id:
    #     data_field.click()
    # elif 'mailing_address' in data_field_id:
    #   if 'primary' in data_field_id:
    #     data_field.click()

  def _yes_no_radio_button(self, fieldset_tag, data_field):
    data_field_id = data_field.get_attribute('id')

    ol_tag = fieldset_tag.find_element_by_tag_name('ol') #grabs the ol tag because its class name contains information about whether button triggers a node to expand
    ol_tag_class = ol_tag.get_attribute('class')

    if 'if' in ol_tag_class or 'location' in ol_tag_class: #the word 'if' indicates that a yes is needed to expand node
      if 'yes' in data_field_id: #if the button's id contains 'yes' then click it
        print 'clicking: ', data_field_id
        data_field.click()
    elif 'not' in ol_tag_class: #the word 'not' indicates that a no is needed to expand node
      if 'no' in data_field_id: #if the button's id contains 'no' then click it
        print 'clicking: ', data_field_id
        data_field.click()

    #if the ol_tag does not have a class name then check the class name if its li tag children
    elif 'if' in ol_tag.find_element_by_tag_name('li').get_attribute('class'): #the word 'if' indicates that a yes is needed to expand node
      if 'yes' in data_field_id: #if the button's id contains 'yes' then click it
        print 'clicking: ', data_field_id
        data_field.click()
    elif 'not' in ol_tag.find_element_by_tag_name('li').get_attribute('class'): #the word 'not' indicates that a no is needed to expand node
      if 'no' in data_field_id: #if the button's id contains 'no' then click it
        print 'clicking: ', data_field_id
        data_field.click()

  def _miscellaneous_radio_button(self, data_field): #handles all of the other radio buttons
    data_field_id = data_field.get_attribute('id')
      
    if 'gender' in data_field_id:
      if 'female' in data_field_id:
        print 'clicking: ', data_field_id
        data_field.click()
    elif 'score_type' in data_field_id:
      if 'manual' in data_field_id:
        data_field.click()
    elif 'marital_status' in data_field_id:
      if 'single' in data_field_id:
        data_field.click()
    elif 'mailing_address' in data_field_id:
      if 'primary' in data_field_id:
        data_field.click()

##############################################################################################################################
  def create_random_username(self):
    self.fake_info.create_random_username()

  def _fill_text_box(self, data_field, page):
    
    print data_field.tag_name, data_field.get_attribute('id'), "sending keys"
    if data_field.is_displayed()==True: #only sends keys to visible text boxes

      if 'autocomplete' in data_field.get_attribute('class'): #autocomplete text boxes
        k = Keys() #used for sending special keys

        if 'degree' in data_field.get_attribute('id'):
          data_field.send_keys('Ma')
        else:
          data_field.send_keys('Mar')
      
        data_field.send_keys(k.ARROW_DOWN) #goes down to first drowdown option
        
        try:
          wait_element = page.ip.is_element_clickable_by_xpath("//li[contains(@class, 'autocomplete')]") #waits for option to load
          highlighted_element = page.driver.find_element_by_xpath("//li[contains(@class, 'autocomplete')]")
          highlighted_element.click() #clicks option
        except Exception, e:
          pass
      elif data_field.get_attribute('autocomplete')=='off': #special dropdown box on payment screen
        k = Keys()
        
        data_field.send_keys('Afghanistan') #did not choose U.S. because extra 'State' box changes
        data_field.send_keys(k.ENTER)
      else:
        try:
          data_field.clear()
          info = self.fake_info.fill_valid_value(data_field)
          data_field.send_keys(info)
        except Exception, e:
          pass
  
  #selects an option from a combo box
  def _select_combo(self, data_field, index):
    print data_field.get_attribute('id'), 'selecting'
    select = Select(data_field)
    select.select_by_index(index)

  def _attach_a_file(self, data_field, div_tag, page):
    data_field = self._check_before_upload(data_field, div_tag, page)

    print '**********'
    print 'Attaching file:', 'test_doc' #file name: 'test_doc.pdf'
    
    print 'path to file:', self.fake_info.path_to_test_doc
    print div_tag.get_attribute('class')
    
    try:
      data_field.send_keys(self.fake_info.path_to_test_doc) #gives file path to input element of type 'file'
    except Exception, e: #fails sometimes due to a change in the DOM, so if that happens we refind the input element and retry
      data_field = div_tag.find_element_by_xpath(".//input[@type='file']")
      data_field.send_keys(self.fake_info.path_to_test_doc)
    
    #wait_element = page.ip.is_text_present_by_xpath(".//a[@class='button']", 'test_doc')
    self._wait_for_upload_to_complete(data_field, div_tag)
    
    print 'Upload Complete'

  def _click_checkbox(self, data_field):
    checkbox = data_field
    #if 'state' not in checkbox.get_attribute('name'):
    if checkbox.is_selected()==False:
      print 'checkbox', checkbox.get_attribute('value')
      checkbox.click()

  def _wait_for_upload_to_complete(self, data_field, div_tag):
    button_name = ''
    timeout = time.time() + 5 #set the wait time for file to upload
    
    while 'test_doc' not in button_name: #keeps checking button text to see if it has changed to the file name
      try:
        time.sleep(.5)
        button_name = div_tag.find_element_by_xpath(".//a[@class='button']").text 
        if 'test_doc' in button_name:
          break
        if time.time() > timeout:
          raise Exception
      except Exception, e:
        print 'file upload failed'
        raise e

  def _check_before_upload(self, data_field, div_tag, page):
    if 'mask' in div_tag.get_attribute('class'):
      upload_button = div_tag.find_element_by_xpath("following-sibling::a[position()=1 and @class='button']") #look for upload button
      upload_button_text = upload_button.text
    else:
      upload_button = div_tag.find_element_by_xpath(".//a[@class='button']") #look for upload button
      upload_button_text = upload_button.text
    
    if 'test_doc' in upload_button_text: #if file is already uploaded then delete it
      delete_button = upload_button.find_element_by_xpath(".//span[contains(@class, 'delete')]")
      delete_button.click()
      alert = page.driver.switch_to_alert()
      alert.accept()
      print '**********'
      print 'previous upload deleted'
      element_after_file_deletion = div_tag.find_element_by_xpath(".//input[@type='file']") #refind input element
      return element_after_file_deletion
    else:
      return data_field                

  def _fill_text_area(self, data_field):
    print data_field.tag_name, data_field.get_attribute('id'), "sending keys"
    if data_field.is_displayed()==True:
      data_field.clear()
      data_field.send_keys(self.fake_info.lorem()[0:100]) #sends 100 character string of placeholder text

  #handles section tags that contain inline in the id
  def _inline_section(self, page, inline_section):
    print 'adding'
    try:
      add_button = inline_section.find_element_by_partial_link_text("Add")
    except Exception, e:
      add_button = inline_section.find_element_by_partial_link_text("recommendation")
    
    #clicks add button for an inline section
    add_button.click()
   
    tr_tag = inline_section.find_element_by_class_name("editing")
    new_forms = tr_tag.find_elements_by_tag_name('form')

    for form in new_forms:
      if 'form' in form.get_attribute('id'):
        self._to_fieldsets(page, form)
      else:
        self._to_all_data_fields(page, form) #used as alternate way of uploading files

    #saves info after filling in section
    save_button = inline_section.find_element_by_partial_link_text("Save")
    save_button.click()
    
    print '**********'
    print 'saving'

    wait_element = page.ip.is_element_visible(add_button)