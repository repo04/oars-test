#!/usr/bin/env python
from pages import LandingPage


def test(args):
  #setup
  driver = args['driver']
  program_url = args['url']
  data = args['data']
  os = args['os']
  
  landing_page = LandingPage(driver, 'Login Page', program_url, os)
  data.create_random_username()

  #test
  landing_page.start_new_app(data)

  email_page = landing_page.navigate_to('Email')
  email_page.sign_in_to_gmail(data)
  email_page.check_for_and_click_email_verification_link(data)
  email_page.switch_to_newest_window()
  
  landing_page.set_password(data)