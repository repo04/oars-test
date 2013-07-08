#!/usr/bin/env python
from selenium import webdriver
import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
      


class Page(object):

  test = None
  program = None
  url = None
  driver = None
  navigation_sections = None

  def __init__(self,args):
   
    self.test = args['test']
    self.program = args['program']
    self.url = args['url']
    self.driver = args['driver']
    
    # creates list of different sections, i.e. Professional Experience
    self.navigation_sections = self.driver.find_elements_by_class_name('icon')
    
  def login(self):
    try:
      self.driver.get(self.url)
    
      existing_application = self.driver.find_element_by_id('choose-sign-in')
      existing_application.click()

      wait = WebDriverWait(self.driver, 5)
      element = wait.until(EC.element_to_be_clickable((By.ID,'id_do_sign_in')))

      email_address = self.driver.find_element_by_name('login')
      password_field = self.driver.find_element_by_name('password')
      sign_in_button = self.driver.find_element_by_id('id_do_sign_in')
    
      email_address.send_keys('ogriffin+OARS1@2u.com')
      password_field.send_keys('qwerty')
      sign_in_button.click()
    except Exception, e:
      print "***Login failed***"
      raise e
    
  def change_password():
    pass
  
  def save_and_signout():
    pass

  def navigate_to(self, index):
     self.navigation_sections[index].click()

  def teardown(self):
    self.driver.close()


  def from_dict(self):
    #page needs to load completely
    time.sleep(4)

    import entryFields 

    fields = entryFields.get_dictionary()
    select = None

    for key in fields.keys():

      #prints out field type first

      #try:
        print '***',fields[key][0],'***'
        if fields[key][0]=='text_box':
          print '***', key,'***'
          text_box = self.driver.find_element_by_id(fields[key][2])
          text_box.clear()
          text_box.send_keys(fields[key][3])

        elif fields[key][0]=='radio_button':
          print '***', key,'***'
          radio_button = self.driver.find_element_by_id(fields[key][2])
          radio_button.click()

          if fields[key][3]!='':
            wait = WebDriverWait(self.driver, 5)
            element = wait.until(EC.element_to_be_clickable((By.ID, fields[key][3])))

        elif fields[key][0]=='combo_box':
          print '***', key,'***'
          combo_box = self.driver.find_element_by_id(fields[key][2])
          select = Select(combo_box)
          select.select_by_visible_text(fields[key][3])

        elif fields[key][0]=='add_button':
          print '***', key, '***'
          add_button = self.driver.find_element_by_link_text(fields[key][2])
          add_button.click()

        elif fields[key][0]=='save_button':
          print '***', key, '***'
          self.driver.execute_script("document.getElementsByClassName('button medium action save')["+fields[key][2]+"].click()")
          
      #except Exception, e:
       # raise e
    time.sleep(8)