#!/usr/bin/env python
from pages import LandingPage


def test(args):
  #setup
  driver = args['driver']
  program_url = args['url']
  data = args['data']
  
  landing_page = LandingPage(driver, 'Login Page', program_url)
  data.create_random_username()
  
  #test
  landing_page.start_new_app(data)

  email_page = landing_page.navigate_to('Email')
  email_page.sign_in_to_gmail(data)
  email_page.check_for_and_click_email_verification_link(data)
  email_page.switch_to_newest_window()
  
  landing_page.set_password(data)

  personal_info = landing_page.navigate_to('Personal Information')
  data.auto_fill(personal_info)
  personal_info.save_and_continue()

  prof_exp = personal_info.navigate_to('Professional Experience')
  data.auto_fill(prof_exp)
  prof_exp.save_and_continue()

  acad_background = prof_exp.navigate_to('Academic Background')
  data.auto_fill(acad_background)
  acad_background.save_and_continue()

  application_uploads = acad_background.navigate_to('Application Uploads')
  data.auto_fill(application_uploads)
  application_uploads.save_and_continue()

  recommendations = application_uploads.navigate_to('Recommendations')
  #needs two recommendations for a complete application
  data.auto_fill(recommendations)
  data.auto_fill(recommendations)
  recommendations.save_and_continue()

  '''recommendations.save_and_signout()
  landing_page.login(data)'''

  landing_page.is_complete(data, [personal_info, prof_exp, acad_background, application_uploads, recommendations])
  
  #recommendations.navigate_to()
  preview_page = landing_page.preview_application()
  preview_page.continue_to_page()
  data.auto_fill(preview_page)
  preview_page.submit()
  preview_page.submit_with_offline_payment()
  preview_page.verify_application_submitted()