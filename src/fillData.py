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
  def auto_fill(self, page): #work in progress
    time.sleep(3)
    print '***START***'
    all_sections = page.driver.find_elements_by_xpath("//section[contains(@id, 'section')]")
    for section in all_sections:
      if section.is_displayed()==True:
        print section.get_attribute('id')
        forms_and_inline_sections = section.find_elements_by_xpath(".//form|.//section[contains(@id, 'inline')]")
        for tag in forms_and_inline_sections:
          print tag.get_attribute('id')
          if tag.tag_name=='form':
            form = tag
            if 'form' in form.get_attribute('id'):
              self._to_fieldsets(page, form)
            else:
              self._to_all_data_fields(page, form) #used as alternate way of uploading files
          elif tag.tag_name=='section':
            inline_section = tag
            self._inline_section(page, inline_section)
        break
    print '***END***'

  def _to_fieldsets(self, page, form):
    fieldsets = form.find_elements_by_tag_name("fieldset")
    for fieldset_tag in fieldsets:
      all_data_fields = fieldset_tag.find_elements_by_xpath(".//select|.//input|.//textarea")
      for data_field in all_data_fields:
        if data_field.is_displayed()==True or 'location' in data_field.get_attribute('id'):
          self._fill(data_field, fieldset_tag, page)

  def _to_all_data_fields(self, page, form):
    all_data_fields = form.find_elements_by_xpath(".//input") #used specifically an alternate way to upload files
    for data_field in all_data_fields:
      if data_field.get_attribute('type')=='file':
        fieldset_tag = data_field.find_element_by_xpath("ancestor::fieldset")
        self._fill(data_field, fieldset_tag, page)

  def _fill(self, data_field, fieldset_tag, page):
      #handles state field in a special manner because the state field switches from a text box
      #to a combo box if the US is selected as the country
    if 'location' in data_field.get_attribute('id'):
      #refinds the state field because it changes from a text box to a combo box depending on the country selected
      state_field = fieldset_tag.find_element_by_xpath(".//select[contains(@id, 'state')]")
      self._select_combo(state_field, 1)
    #checks to see if a text field is visible then sends keys.
    elif data_field.get_attribute('type')=='text' or data_field.get_attribute('type')=='email': #and field.is_displayed()==True:
      self._fill_text_box(data_field, page)

      #selects yes or no depending on whether button triggers a node to expand
    elif data_field.get_attribute('type')=='radio':
      self._click_radio(data_field, fieldset_tag)
        
      #selects the first option in combo boxes
    elif data_field.tag_name=='select':
      self._select_combo(data_field, 1)

    elif data_field.get_attribute('type')=='file':
      self._attach_a_file(data_field, fieldset_tag, page)

    elif data_field.get_attribute('type')=='checkbox':
      self._click_checkbox(data_field)

    elif data_field.tag_name=='textarea':
      self._fill_text_area(data_field)

  def _click_radio(self, data_field, fieldset_tag):
    data_field_id = data_field.get_attribute('id')
    if 'yes' in data_field_id or 'no' in data_field_id:
      #choose to expand node or else pick yes by default
      try:
        ol_tag = fieldset_tag.find_element_by_tag_name('ol')
        if 'if' in ol_tag.get_attribute('class') or 'location' in ol_tag.get_attribute('class'):
          if 'yes' in data_field_id:
            print 'clicking: ', data_field_id
            data_field.click()
        elif 'not' in ol_tag.get_attribute('class'):
          if 'no' in data_field_id:
            print 'clicking: ', data_field_id
            data_field.click()
        elif 'if' in ol_tag.find_element_by_tag_name('li').get_attribute('class'):
          if 'yes' in data_field_id:
            print 'clicking: ', data_field_id
            data_field.click()
        elif 'not' in ol_tag.find_element_by_tag_name('li').get_attribute('class'):
          if 'no' in data_field_id:
            print 'clicking: ', data_field_id
            data_field.click()
      except Exception, e:
        if 'yes' in data_field_id:
          print 'clicking: ', data_field_id
          data_field.click()
    elif 'gender' in data_field_id:
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
    #elif 'offline' in data_field.get_attribute('id'): #payment screen
    #  pass
##############################################################################################################################
  def create_random_username(self):
    self.fake_info.create_random_username()

  def _fill_text_box(self, data_field, page):
    
    print data_field.tag_name, data_field.get_attribute('id'), "sending keys"
    if data_field.is_displayed()==True:
      if 'autocomplete' in data_field.get_attribute('class'):
        k = Keys()
        #temp value: 'Ma' is temporarily being used because it is triggering the autocomplete dropdown for the three autocomplete textboxes
        data_field.send_keys('Mar')
      
        data_field.send_keys(k.ARROW_DOWN)
        
        try:
          wait_element = page.ip.is_element_clickable_by_xpath("//li[contains(@class, 'autocomplete')]")
          highlighted_element = page.driver.find_element_by_xpath("//li[contains(@class, 'autocomplete')]")
          highlighted_element.click()
        except Exception, e:
          pass
      else:
        data_field.clear()
        info = self.fake_info.fill_valid_value(data_field)
        data_field.send_keys(info)
  
  #selects an option from a combo box
  def _select_combo(self, data_field, index):
    print data_field.get_attribute('id'), 'selecting'
    select = Select(data_field)
    select.select_by_index(index)

  def _attach_a_file(self, data_field, fieldset_tag, page):
    '''if fieldset_tag==None:
      pass'''

    data_field = self._check_before_upload(data_field, fieldset_tag, page)

    print '**********'
    print 'Attaching file:', 'test_doc'
    
    #path to 
    print 'path to file:', self.fake_info.path_to_test_doc
    #gives file path to input element
    try:
      data_field.send_keys(self.fake_info.path_to_test_doc)
    except Exception, e:
      print 'upload failed'
      print 'trying again'
      data_field = fieldset_tag.find_element_by_xpath(".//input[@type='file']")
      data_field.send_keys(self.fake_info.path_to_test_doc)
    
    self._wait_for_upload_to_complete(data_field, fieldset_tag)
    
    print 'Upload Complete'

  def _click_checkbox(self, data_field):
    checkbox = data_field
    if checkbox.is_selected()==False:
      print 'checkbox', checkbox.get_attribute('value')
      checkbox.click()

  def _wait_for_upload_to_complete(self, data_field, fieldset_tag):
    button_name = ''
    while 'test_doc' not in button_name:
      try:
        button_name = fieldset_tag.find_element_by_xpath(".//a[@class='button']").text
      except Exception, e:
        pass

  def _check_before_upload(self, data_field, fieldset_tag, page):
    upload_button = fieldset_tag.find_element_by_xpath(".//a[@class='button']")
    upload_button_text = upload_button.text
    if 'test_doc' in upload_button_text:
      delete_button = upload_button.find_element_by_xpath(".//span[contains(@class, 'delete')]")
      delete_button.click()
      alert = page.driver.switch_to_alert()
      alert.accept()
      print '**********'
      print 'previous upload deleted'
      element_after_file_deletion = fieldset_tag.find_element_by_xpath(".//input[@type='file']")
      return element_after_file_deletion
    else:
      return data_field                

  def _fill_text_area(self, data_field): #not tested yet
    print data_field.tag_name, data_field.get_attribute('id'), "sending keys"
    if data_field.is_displayed()==True:
      data_field.clear()
      data_field.send_keys(self.fake_info.lorem()[0:100])

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
    new_form = tr_tag.find_element_by_tag_name('form')

    self._to_fieldsets(page, new_form)

    #saves info after filling in section
    save_button = inline_section.find_element_by_partial_link_text("Save")
    save_button.click()
    
    print '**********'
    print 'saving'

    wait_element = page.ip.is_element_visible(add_button)
    #wait_element = page.ip.is_element_clickable_by_xpath(".//a[contains(@class, 'button medium action save')]")
