#!/usr/bin/env python
from pages import LandingPage


def test(args):
  #setup
  driver = args['driver']
  program_url = args['url']
  data = args['data']
  
  landing_page = LandingPage(driver, 'Login Page', program_url)
  landing_page.login(data)

  #test
  '''landing_page.start_new_app(data)

  email_page = landing_page.navigate_to('Email')
  email_page.sign_in_to_gmail(data)
  email_page.check_for_and_click_email_verification_link(data)
  email_page.switch_to_newest_window()
  
  landing_page.set_password(data)

  personal_info = landing_page.navigate_to('Personal Information')
  data.auto_fill(personal_info)
  
  prof_exp = personal_info.navigate_to('Professional Experience')
  data.auto_fill(prof_exp)

  acad_background = prof_exp.navigate_to('Academic Background')
  data.auto_fill(acad_background)

  application_uploads = acad_background.navigate_to('Application Uploads')
  data.auto_fill(application_uploads)

  recommendations = application_uploads.navigate_to('Recommendations')
  #needs two recommendations for complete application
  data.auto_fill(recommendations)
  data.auto_fill(recommendations)'''

  preview_page = landing_page.preview_application()
  preview_page.continue_to_page()
  data.auto_fill(preview_page)
  preview_page.submit()