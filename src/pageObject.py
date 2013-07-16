#!/usr/bin/env python
from selenium import webdriver
import time, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import personalInformation, professionalExperience, academicBackground     
import fakeInfo



class Page(object):

  test = None
  program = None
  url = None
  driver = None
  
  navigation_sections = None
  index = None
  wait = None
  fake_info = None

  sections = personalInformation, professionalExperience, academicBackground, '', ''

  def __init__(self, args, index = None):
    self.test = args['test']
    self.program = args['program']
    self.url = args['url']
    self.driver = args['driver']
    
    self.index = index
    self.wait = WebDriverWait(self.driver, 5)

    # creates list of different sections, i.e. Professional Experience
    self.navigation_sections = self.driver.find_elements_by_class_name('icon')

    self.fake_info = fakeInfo.FakeData()

  def login(self):
    try:
      self.driver.get(self.url)
    
      existing_application = self.driver.find_element_by_id('choose-sign-in')
      existing_application.click()

      element = self.wait.until(EC.element_to_be_clickable((By.ID,'id_do_sign_in')))

      email_address = self.driver.find_element_by_name('login')
      password_field = self.driver.find_element_by_name('password')
      sign_in_button = self.driver.find_element_by_id('id_do_sign_in')
    
      email_address.send_keys('ogriffin+OARS1@2u.com')
      password_field.send_keys('qwerty')
      sign_in_button.click()

      element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'icon')))
    except Exception, e:
      print "***Login failed***"
      raise e
    
  def change_password(self):
    change_password_button = self.driver.find_element_by_class_name('action leave reset-password')
    change_password_button.click()
  
  def save_and_signout(self):
    sign_out_button = self.driver.find_element_by_id('id_do_sign_out')
    sign_out_button.click()
    alert = self.driver.switch_to_alert()
    alert.accept()
    element = self.wait.until(EC.element_to_be_clickable((By.ID, 'id_email')))

  def navigate_to(self):
    try:
      self.navigation_sections[self.index].click()
    except Exception, e:
      raise e 

  def teardown(self):
    self.driver.close()


  '''def complete(self):
    form = self.sections[self.index].info()

    for field in form:
      #try:
        #prints out field type first
        print '***',form[field][0],'***'
        if form[field][0]=='text_box':
          print '***', field,'***'
          text_box = self.driver.find_element_by_id(form[field][2])
          text_box.clear()
          text_box.send_keys(form[field][3])

        elif form[field][0]=='radio_button':
          print '***', field,'***'
          radio_button = self.driver.find_element_by_id(form[field][2])
          radio_button.click()

          if form[field][3]!='':
            element = self.wait.until(EC.element_to_be_clickable((By.ID, form[field][3])))

        elif form[field][0]=='combo_box':
          print '***', field,'***'
          combo_box = self.driver.find_element_by_id(form[field][2])
          select = Select(combo_box)
          select.select_by_visible_text(form[field][3])

        elif form[field][0]=='add_button':
          print '***', field, '***'
          add_button = self.driver.find_element_by_link_text(form[field][2])
          add_button.click()

        elif form[field][0]=='save_button':
          print '***', field, '***'
          self.driver.execute_script("document.getElementsByClassName('button medium action save')["+form[field][2]+"].click()")
        
        elif form[field][0]=='attach_a_file':
          print '***', field, '***'
          attach_button = self.driver.find_element_by_name(form[field][2])
          attach_button.send_keys(form[field][3])
      #except Exception, e:
       # raise e'''

#alternate way of filling section below

  def _fill_text(self, element):
    
    print element.tag_name, element.get_attribute('id'), "sending keys"
    
    if 'autocomplete' in element.get_attribute('class'):
      k = Keys()
      #temp value: 'Mar' is temporarily being used because it is triggering the autocomplete dropdown for the three autocomplete textboxes
      element.send_keys('Mar')
      
      element.send_keys(k.ARROW_DOWN)
      
      self.wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'autocomplete')]")))
      
      highlighted_element = self.driver.find_element_by_xpath("//li[contains(@class, 'autocomplete')]")
      highlighted_element.click()

    else:
      element.clear()
      info = self.fake_info.fill_valid_value(element)
      element.send_keys(info)
    
  def _select_combo(self, element, option):
    print element.get_attribute('id'), 'selecting'
    select = Select(element)
    select.select_by_index(option)

  def _click_radio(self, element, fieldset):
    print "radio button"

    #finds all children of fieldset tag
    for sub_node in fieldset.find_elements_by_xpath("*"):
      #iterates through child nodes until it finds the ol child
      #the ol child would carry information about whether or not the radio button is linked to hidden data fields
      if sub_node.tag_name=='ol':
        #for radio buttons where a 'yes' would expand a hidden node, the words 'if' or 'location' are used in the ol class attribute
        if 'if' in sub_node.get_attribute('class') or 'location' in sub_node.get_attribute('class'):
          #since 'if' is in the class attribute field we want to find and click the 'yes' radio button
          if 'yes' in element.get_attribute('id'):
            print element.get_attribute('id'), 'yes'
            element.click()
        #for radio buttons where a 'no' would expand a hidden node, the word 'not' is used in the ol class attribute
        elif'not' in sub_node.get_attribute('class'):
          #since 'not' is in the class attribute field we want to find and click the 'no' radio button
          if 'no' in element.get_attribute('id'):
            print element.get_attribute('id'), 'no'
            element.click()

  def _inline_section(self, element):
    print 'adding'
    add_button = element.find_element_by_xpath(".//a[contains(@class, 'button action medium add')]")
    save_button = element.find_element_by_xpath(".//a[contains(@class, 'button medium action save')]")
  
    #clicks add button for an inline section
    add_button.click()
   
    #finds input, select and fieldset tags for the newly expanded inline section    
    sub_tr = element.find_element_by_xpath(".//tr[@class='editing']")
    inputs = sub_tr.find_elements_by_xpath(".//input[@id!='']|.//select[@id!='']")
    fieldset = sub_tr.find_element_by_xpath(".//fieldset")
    
    self._sort_and_fill(inputs, fieldset)
    
    #saves info after filling in section
    save_button.click()

    print 'saving'

  def _sort_and_fill(self, inputs, fieldset=None):
    index = 0

    while index < len(inputs):
      field = inputs[index]
      print '*********'
      
      #handles state field in a special manner because the state field switches from a text box
      #to a combo box if the US is selected as the country
      if 'location' in field.get_attribute('id'):
        state_field = fieldset.find_element_by_xpath(".//select[contains(@id, 'state')]")
        self._select_combo(state_field, 1)
      
      #checks to see if a text field is visible then sends keys.
      elif field.get_attribute('type')=='text' and field.is_displayed()==True:
        self._fill_text(field)

      #selects yes or no depending on whether button triggers a node to expand
      elif field.get_attribute('type')=='radio':
        self._click_radio(field, fieldset)
        
      #selects the first option in combo boxes
      elif field.tag_name=='select':
        self._select_combo(field, 1)
      
      index += 1 

  def auto_fill(self):
    #temporary. wait for page to load.
    time.sleep(3)

    #grabs anything with either a fieldset tag or section tag contiaining the word 'inline' in its id field
    fieldsets_inlines = self.driver.find_elements_by_xpath("//fieldset|//section[contains(@id, 'inline')]")

    print '***start***'

    #iterates through fieldsets_inlines list and for each fieldset/section tag, finds the input
    #and/or select elements, then interacts with them appropriately
    for tag in fieldsets_inlines:
      #only evaluates elements on current page
      if tag.is_displayed()==True:
        if tag.tag_name=='fieldset':
          inputs = tag.find_elements_by_xpath(".//select[@id!='']|.//input[@id!='']")
          #calls _sort_and_fill() method using input/select element and the fieldset tag of its ancestral node 
          self._sort_and_fill(inputs, tag)
        elif tag.tag_name=='section':
          self._inline_section(tag)
    
    print '***end***'