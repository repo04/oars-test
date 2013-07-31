#!/usr/bin/env python
import time, sys
from pageObject import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LandingPage(Page):
  def __init__(self, driver, name, url):
    if driver=='Chrome':
      driver = webdriver.Chrome('./src/resources/chromedriver')
    else: #instantiate Firefox by default
      driver = webdriver.Firefox()
    #initialize parent class
    super(LandingPage, self).__init__(driver, name)
    self.driver.get(url)

  def start_new_app(self, data):  #to be relocated
    
    first_time_applying = self.driver.find_element_by_id('choose-start-app')    
    first_time_applying.click()

    email_address_field = self.driver.find_element_by_id('id_email')
    first_name_field = self.driver.find_element_by_id('id_first_name')
    last_name_field = self.driver.find_element_by_id('id_last_name')
    
    first_name = data.fake_info.fill_valid_value(last_name_field)
    last_name = data.fake_info.fill_valid_value(first_name_field)
    email_address = data.fake_info.email

    email_address_field.send_keys(email_address)
    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)

    start_a_new_application = self.driver.find_element_by_partial_link_text("new application")
    start_a_new_application.click()

  def set_password(self, data):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.ID, 'in_password')))
    
    print '**********'
    print 'setting password'

    new_password_field = self.driver.find_element_by_id('in_password')
    confirm_new_password_field = self.driver.find_element_by_id('in_confirm_password')
    set_new_password_button = self.driver.find_element_by_partial_link_text("Set my password")

    new_password_field.send_keys(data.fake_info.password)
    confirm_new_password_field.send_keys(data.fake_info.password)
    set_new_password_button.click()

    wait_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'big button')]")))

    print '**********'
    print 'new user created: '+data.fake_info.email+'\n'
    print '\nWelcome to OARS!\n'

    try:
      welcome_banner = self.driver.find_element_by_xpath("//a[@class='close']")
      welcome_banner.click()
    except Exception, e:
      pass

  def login(self, data):
    #try:
    existing_application = self.driver.find_element_by_id('choose-sign-in')
    existing_application.click()

    wait_element = self.wait.until(EC.element_to_be_clickable((By.ID,'id_do_sign_in')))

    email_address_field = self.driver.find_element_by_id('id_login')
    password_field = self.driver.find_element_by_id('id_password')
    sign_in_button = self.driver.find_element_by_id('id_do_sign_in')

    email_address_field.send_keys(data.fake_info.email)
    password_field.send_keys(data.fake_info.password)
    
    print '**********'
    print 'logging in'
    sign_in_button.click()

    wait_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'big button')]")))
    # except Exception, e:
    #  print "***Login failed***"
     # raise e

class PreviewPage(Page):
  def __init__(self, driver, name):
    super(PreviewPage, self).__init__(driver, name)

  def continue_to_page(self):
    try:
      '''wait_element = self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/nav/a[2]')))
      continue_button = self.driver.find_element_by_xpath('/html/body/div[2]/nav/a[2]') #/span'''
      wait_element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Continue')))
      continue_button = self.driver.find_element_by_link_text("Continue")
      continue_button.click()
    except Exception, e:
      pass
    print '**********'
    print 'continuing to submission page'
    
    #html.js body div#DOMWindow nav.preview a.button
    '''self.driver.switch_to_frame(0)
    continue_button = self.driver.find_element_by_link_text("//class[contains(@class, 'closeDOMWindow')]")
    continue_button.click()'''

  def submit(self):
    try:
      submit_button = self.driver.find_element_by_partial_link_text("Submit")
      submit_button.click()
    except Exception, e:
      pass

  def submit_with_offline_payment(self):
    self.driver.switch_to_frame(1)
    wait_element = self.wait.until(EC.element_to_be_clickable((By.ID,'id_payment_method.offline')))
    offline_payment_button = self.driver.find_element_by_xpath("//input[contains(@id, 'offline')]")
    offline_payment_button.click()

    wait_element = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Continue')))
    continue_button = self.driver.find_element_by_partial_link_text("Continue")
    print '**********'
    print 'clicking continue'
    continue_button.click()

    wait_element = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Continue')))
    continue_button_2 = self.driver.find_element_by_partial_link_text("Continue")
    print '**********'
    print 'clicking continue'
    continue_button_2.click()

    self.driver.switch_to_default_content()

    #time.sleep(30)

  def verify_application_submitted(self):
    print '**********'
    print 'verifying that application has been submitted'
    '''application_submitted_button = self.driver.find_element_by_xpath("//a[contains(text(), 'Application Submitted')]")
    wait_element = self.wait.until(EC.visibility_of(application_submitted_button))
    
    application_submitted = None #boolean
    #action submitted
    while application_submitted != True:
      try:
        application_submitted_button = self.driver.find_element_by_xpath("//a[contains(text(), 'Application Submitted')]")
        application_submitted = application_submitted_button.is_displayed()
      except Exception, e:
        pass'''

    print '**********'
    print 'application complete'

class EmailPage(Page):
  def __init__(self, driver, name):
    super(EmailPage, self).__init__(driver, name)
    print '**********'
    print 'navigating to', name
    self.driver.get('https://gmail.com')
      
  def sign_in_to_gmail(self, data):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.ID,'Email')))

    username_field = self.driver.find_element_by_id('Email')
    password_field = self.driver.find_element_by_id('Passwd')
    sign_in_button = self.driver.find_element_by_xpath("//input[@type='submit']")

    username_field.send_keys(data.fake_info.gmail)
    password_field.send_keys(data.fake_info.password)
    sign_in_button.click()

  def check_for_and_click_email_verification_link(self, data):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@email,'.edu')]")))
    
    email_from_program = self.driver.find_element_by_xpath("//span[contains(@email,'.edu')]")
    
    email_from_program.click()
  
    wait_element = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, data.program_url)))

    #grabs all possible links in email. others may exist in the same email
    #thread due to the test being run multiple times
    verification_links = self.driver.find_elements_by_xpath("//a[contains(@href, '"+data.program_url+"')]")
    
    print '**********'
    print 'opening confirmation email and clicking verification link'    

    for link in verification_links:
      if link.is_displayed()==True:
        print '**********'
        print 'clicking link'
        link.click()
        #break

  '''while self._has_new_window_loaded==True:
      pass

  def _has_new_window_loaded(self):
    for handle in self.driver.window_handles:
      self.driver.switch_to_window(handle)
      print self.driver.title
      if '2U Mail' not in self.driver.title:
        print '**********'
        print 'switching windows to: '+self.driver.title
        return True
      return False

    latest_window = self.driver.window_handles[-1]
    self.driver.switch_to_window(latest_window)
    print '**********'
    print 'switching windows to: '+self.driver.title

class PersonalInformation(page):
  def __init__(self, driver, name):
    super(PersonalInformation, self).__init__(driver, name)
    
class ProfessionalExperience(page):
  def __init__(self, driver, name):
    super(ProfessionalExperience, self).__init__(driver, name)
  
class AcademicBackground(page):
  def __init__(self, driver, name):
    super(AcademicBackground, self).__init__(driver, name)
    
class ApplicationUploads(page):
  def __init__(self, driver, name):
    super(ApplicationUploads, self).__init__(driver, name)

class Recommendations(page):
  def __init__(self, driver, name):
    super(Recommendations, self).__init__(driver, name)'''
