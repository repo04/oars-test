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
  
  prof_exp = personal_info.navigate_to('Professional Experience')
  data.auto_fill(prof_exp)

  acad_background = prof_exp.navigate_to('Academic Background')
  data.auto_fill(acad_background)

  application_uploads = acad_background.navigate_to('Application Uploads')
  data.auto_fill(application_uploads)

  recommendations = application_uploads.navigate_to('Recommendations')
  #needs two recommendations for a complete application
  data.auto_fill(recommendations)