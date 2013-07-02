#!/usr/bin/env python
from selenium import webdriver
import time
import sys
#sys.path.insert(0, './test')
import superTest
#sys.path.insert(0, '../../oars-tests')

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
    
  def login(self, program_url):
    self.driver.get(program_url)
    
    existing_application = self.driver.find_element_by_id('choose-sign-in')
    existing_application.click()
    
    email_address = self.driver.find_element_by_name('login')
    password_field = self.driver.find_element_by_name('password')
    sign_in_button = self.driver.find_element_by_id('id_do_sign_in')
    
    email_address.send_keys('ogriffin+OARS1@2u.com')
    password_field.send_keys('qwerty')
    sign_in_button.click()        
    
  def change_password():
    pass
  
  def save_and_signout():
    pass

  def navigate_to(self, index):
     self.navigation_sections[index].click()

  def teardown(self):
    self.driver.close()