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

  def __init__(self, args):
   
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

      element2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon')))
    except Exception, e:
      print "***Login failed***"
      raise e
    
  def change_password():
    pass
  
  def save_and_signout():
    pass

  def navigate_to(self):
     pass

  def teardown(self):
    self.driver.close()


  def complete(self):

    #page needs to load completely; replace with webdriverwait
    time.sleep(4)

    import personalInformation 

    form = personalInformation.complete()
    select = None

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
            wait = WebDriverWait(self.driver, 5)
            element = wait.until(EC.element_to_be_clickable((By.ID, form[field][3])))

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
          
      #except Exception, e:
       # raise e
    time.sleep(8)