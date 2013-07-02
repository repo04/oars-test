#!/usr/bin/env python
from selenium import webdriver
import time
import sys

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

      from selenium.webdriver.common.by import By
      from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
      from selenium.webdriver.support import expected_conditions as EC
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
    #sys.path.insert(0, './src/')
    import entryFields 

    for key in entryFields.get_dictionary():
      print key
      '''
      if key=='text_box':
        driver.send_keys(key[3])
      elif key=='radio_button':
        driver.click()
      elif key=='combo_box':
        pass'''
      