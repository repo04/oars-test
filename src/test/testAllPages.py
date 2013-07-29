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
  recommendations.save_and_continue()