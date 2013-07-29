#!/usr/bin/env python
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):

  driver = None  
  wait = None
  name = None

  def __init__(self, driver, name = None):
    self.driver = driver
    self.wait = WebDriverWait(self.driver, 45)
    self.name = name

  
  def change_password(self):
    change_password_button = self.driver.find_element_by_class_name('action leave reset-password')
    change_password_button.click()
  
  def save_and_signout(self):
    sign_out_button = self.driver.find_element_by_id('id_do_sign_out')
    sign_out_button.click()
    alert = self.driver.switch_to_alert()
    alert.accept()
    wait_element = self.wait.until(EC.element_to_be_clickable((By.ID, 'id_email')))

  def save_and_continue(self):
    try:
      #save_and_continue_button = self.driver.find_element_by_xpath("//a[text()='Save & Continue']")
      save_and_continue_button = self.driver.find_element_by_link_text("Save & Continue")
      save_and_continue_button.click()
    except Exception, e:
      pass

  def preview_application(self):
    time.sleep(3)
    preview_application_button = self.driver.find_element_by_partial_link_text("Preview Your Application")
    preview_application_button.click()
    #preview_application_button = self.driver.find_element_by_xpath("//a[text()='Preview Your Application']")
    from pages import PreviewPage
    preview_page = PreviewPage(self.driver, 'Preview')
    return preview_page

  def teardown(self):
    print '**********'
    print 'closing'
    self.driver.close()

  #looks for and clicks page_name's corresponding link in the navbar; instantiates and returns a Page object.
  #if 'Email' is passed, then an EmailPage object is instantiated and returned instead.
  def navigate_to(self, page_name):
    if page_name=='Email':
      from pages import EmailPage
      email_page = EmailPage(self.driver, page_name)
      return email_page
    else:
      link_to_next_page = self.driver.find_element_by_partial_link_text(page_name)
      #link_to_next_page = self.driver.find_element_by_xpath("//a[text()='"+page_name+"']")
      next_page = Page(self.driver, page_name)

      print '**********'
      print 'navigating to', next_page.name
      link_to_next_page.click()
      return next_page

  #short wait then driver switches to the last window opened
  def switch_to_newest_window(self):
    #sleep to be replaced by self.has_new_window_loaded()
    time.sleep(4)

    latest_window = self.driver.window_handles[-1]
    self.driver.switch_to_window(latest_window)
    print '**********'
    print 'window switched to: '+self.driver.title