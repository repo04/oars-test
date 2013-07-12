#!/usr/bin/env python
from selenium import webdriver
import time, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import personalInformation, professionalExperience, academicBackground
from faker import Faker     

class Page(object):

  test = None
  program = None
  url = None
  driver = None
  
  navigation_sections = None
  index = None
  wait = None

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

      time.sleep(2) #temporary
    except Exception, e:
      raise e 

  def teardown(self):
    self.driver.close()


  def complete(self):
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
       # raise e

#alternate way of filling section below

  def _fill_text(self, element):
    print element.tag_name, element.get_attribute('id'), "sending keys"
    element.clear()
    element.send_keys("stuff")

  def _select_combo(self, element, option):
    print element.get_attribute('id'), 'selecting'
    select = Select(element)
    select.select_by_index(option)

  def _click_radio(self, element, fieldset):
    print "radio button"
    if len(fieldset.find_elements_by_xpath("*"))==2 and 'if' in fieldset.find_element_by_xpath("ol").get_attribute('class'):
      if 'yes' in element.get_attribute('id'):
        print element.get_attribute('id'), 'yes'
        element.click()
    elif len(fieldset.find_elements_by_xpath("*"))==2 and 'not' in fieldset.find_element_by_xpath("ol").get_attribute('class'):
      if 'no' in element.get_attribute('id'):
        print element.get_attribute('id'), 'no'
        element.click()

  def _inline_section(self, element):
    print 'adding'
    buttons = element.find_elements_by_xpath(".//a[contains(@class, 'button')]")
    print len(buttons)
    add_button = buttons[2]
    save_button = buttons[3]

    add_button.click()
    
    sub_tr = element.find_element_by_xpath(".//tr[@class='editing']")
    inputs = sub_tr.find_elements_by_xpath(".//input[@id!='']|.//select[@id!='']")
    for input in inputs:
      print input.get_attribute('id')

    self._sort_and_fill(inputs)

    save_button.click()

    print 'saving'

  def _sort_and_fill(self, inputs, fieldset=None):
    index = 0
    while index < len(inputs):
      field = inputs[index]
      #send keys to text field
      if field.get_attribute('type')=='text' and field.is_displayed()==True:  #temp: and 'other' not in field.get_attribute('id')
        if 'location' not in field.get_attribute('id'): 
          self._fill_text(field)
          pass
      #select yes or no depending on whether button triggers a node to expand
      elif field.get_attribute('type')=='radio':
        self._click_radio(field, fieldset)
        pass
        #select combo boxes
      elif field.tag_name=='select':
        self._select_combo(field, 1)
        
        #handles add sections
      elif field.tag_name=='section' and 'inline' in field.get_attribute('id'):
        print field.get_attribute('id')
        self._inline_section(field)
      index += 1 

  def auto_fill(self):
    #info = Faker()
    time.sleep(3)
    #sections = self.driver.find_elements_by_xpath("//select[@id!='']|//input[@id!='']")
    #conditionals = self.driver.find_elements_by_xpath("//ol[contains(@class, 'conditional')]|//ol[contains(@class, 'if')]")
    
    #grabs anything with a form tag
    forms = self.driver.find_elements_by_xpath("//form")
    forms_fieldsets = []
    num = 0

    #makes a list of all fieldset section tags before professional experience section; temp: fix to grad inline sections as well
    while 'professional' not in forms[num].get_attribute('id'):
      forms_fieldsets += forms[num].find_elements_by_xpath("fieldset")
      num += 1

    print '***start***'
    
    #rough draft
    #iterates thru forms_fieldsets list and for each fieldset tag find the input and/or select elements and interact with them appropriately
    for fieldset in forms_fieldsets:
      #grabs anything with a select or input tag starting from fieldset node
      inputs = fieldset.find_elements_by_xpath(".//select[@id!='']|.//input[@id!='']")
      self._sort_and_fill(inputs, fieldset)
    

    inlines = self.driver.find_elements_by_xpath("//section[contains(@id, 'inline')]")
    self._sort_and_fill(inlines)

    print '***end***'