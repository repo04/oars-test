#!/usr/bin/env python
from pageObject import Page
from selenium import webdriver
import time
import sys

class LandingPage(Page):
  def __init__(self, driver, name, url, os):
    #===========================================================================
    # if driver.lower()=='chrome':
    #   driver = webdriver.Chrome('C:/Python27/Scripts/chromedriver.exe')
    # elif driver.lower()=='firefox':
    #   driver = webdriver.Firefox()
    #   driver.maximize_window() # does not work with chrome
    #===========================================================================
    
    global desired_capabilities
    
    if driver.lower() == 'chrome':
      desired_capabilities = webdriver.DesiredCapabilities.CHROME
    else:
      #driver.lower() == 'firefox':
      desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
      #desired_capabilities['version'] = '22'
    
    if os == 'mac':
      desired_capabilities['platform'] = 'MAC'
      desired_capabilities['name'] = 'MAC' + '_' + driver.lower()
    elif os == 'linux32' or os == 'linux64':
      desired_capabilities['platform'] = 'LINUX'
      desired_capabilities['name'] = 'LINUX' + '_' + driver.lower()
    else:
      desired_capabilities['platform'] = 'WINDOWS 8'
      desired_capabilities['name'] = 'WINDOWS 8' + '_' + driver.lower()         


    self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://someshbansal:10c353c4-24e9-434c-811d-f3aba9e14213@ondemand.saucelabs.com:80/wd/hub"
        )
    super(LandingPage, self).__init__(self.driver, name)  # initialize parent class
    self.driver.get(url)

  def start_new_app(self, data):
    
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
    wait_element = self.ip.is_element_clickable_by_id('in_password')

    print '**********'
    print 'setting password'

    new_password_field = self.driver.find_element_by_id('in_password')
    confirm_new_password_field = self.driver.find_element_by_id('in_confirm_password')
    set_new_password_button = self.driver.find_element_by_partial_link_text("Set my password")

    new_password_field.send_keys(data.fake_info.password)
    confirm_new_password_field.send_keys(data.fake_info.password)
    set_new_password_button.click()

    wait_element = self.ip.is_element_clickable_by_xpath("//a[contains(@class, 'big button')]")

    print '**********'
    print 'new user created: ' + data.fake_info.email + '\n'
    print '\nWelcome to OARS!\n'

    try:
      welcome_banner = self.driver.find_element_by_class_name("close")
      welcome_banner.click()
    except Exception, e:
      pass

  def login(self, data):
    existing_application = self.driver.find_element_by_id('choose-sign-in')
    existing_application.click()

    wait_element = self.ip.is_element_clickable_by_id('id_do_sign_in')

    email_address_field = self.driver.find_element_by_id('id_login')
    password_field = self.driver.find_element_by_id('id_password')
    sign_in_button = self.driver.find_element_by_id('id_do_sign_in')

    email_address_field.send_keys(data.fake_info.email)
    password_field.send_keys(data.fake_info.password)
    
    print '**********'
    print 'logging in'
    sign_in_button.click()

    wait_element = self.ip.is_element_clickable_by_xpath("//a[contains(@class, 'big button')]")
    
  def get_all_pages_from_navbar(self):
    all_pages = []

    navbar = self.driver.find_element_by_class_name('sections')
    link_to_all_pages = navbar.find_elements_by_tag_name('a')
    for link in link_to_all_pages:
      all_pages.append(Page(self.driver, link.text))
    
    return all_pages

class PreviewPage(Page):
  def __init__(self, driver, name):
    super(PreviewPage, self).__init__(driver, name)

  def continue_to_page(self):
    try:
      wait_element = self.ip.is_element_clickable_by_link_text('Continue')
      continue_button = self.driver.find_element_by_link_text('Continue')
      continue_button.click()
    except Exception, e:
      pass
    print '**********'
    print 'continuing to submission page'

  def submit(self):
    try:
      submit_button = self.driver.find_element_by_partial_link_text("Submit")
      submit_button.click()
    except Exception, e:
      pass

  def confirm_submit(self, data):
    try:
      self.driver.switch_to_frame(1)
      try:
        offline_payment_button = self.driver.find_element_by_xpath("//input[contains(@id, 'offline')]")
        offline_payment_button.click()
      except Exception, e:
        pass
      try:
        continue_button = self.driver.find_element_by_partial_link_text("Continue")
        print '**********'
        print 'clicking continue'
        continue_button.click()
      except Exception, e:
        pass
      try:
        data.auto_fill_iframe(self)
      except Exception, e:
        pass
      try:
        continue_button_2 = self.driver.find_element_by_partial_link_text("Continue")
        print '**********'
        print 'clicking continue'
        continue_button_2.click()
      except Exception, e:
        submit_button = self.driver.find_element_by_partial_link_text("Submit")
        print '**********'
        print 'submitting'
        submit_button.click()

      self.driver.switch_to_default_content()

    except Exception, e:
      pass

  def verify_application_submitted(self):  # needs work
    print '**********'
    print 'verifying that application has been submitted'
    
    try:  # checks for 'Application Complete'. if check fails, then it checks again but for upper case string
      wait_element = self.ip.is_text_present_by_xpath("//a[contains(@class, 'submitted')]", 'Application Submitted')
    except Exception, e:
      wait_element = self.ip.is_text_present_by_xpath("//a[contains(@class, 'submitted')]", 'Application Submitted'.upper())
    
    print '**********'
    print 'application complete'

class EmailPage(Page):
  def __init__(self, driver, name):
    super(EmailPage, self).__init__(driver, name)
    print '**********'
    print 'navigating to', name
    self.driver.get('https://gmail.com')
      
  def sign_in_to_gmail(self, data):
    wait_element = self.ip.is_element_clickable_by_id('Email')

    username_field = self.driver.find_element_by_id('Email')
    password_field = self.driver.find_element_by_id('Passwd')
    sign_in_button = self.driver.find_element_by_xpath("//input[@type='submit']")

    username_field.send_keys(data.fake_info.gmail)
    password_field.send_keys(data.fake_info.password)
    sign_in_button.click()

  def check_for_and_click_email_verification_link(self, data):
    wait_element = self.ip.is_element_clickable_by_xpath("//span[contains(@email,'.edu')]")

    email_from_program = self.driver.find_element_by_xpath("//span[contains(@email,'.edu')]")
    
    email_from_program.click()
  
    # wait_element = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, data.program_url)))
    wait_element = self.ip.is_element_clickable_by_partial_link_text(data.program_url)
    # grabs all possible links in email. others may exist in the same email
    # thread due to the test being run multiple times
    verification_links = self.driver.find_elements_by_xpath("//a[contains(@href, '" + data.program_url + "')]")
    
    print '**********'
    print 'opening confirmation email and clicking verification link'    

    for link in verification_links:
      if link.is_displayed() == True:
        print '**********'
        print 'clicking link'
        link.click()
        break

'''class PersonalInformation(page):
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
