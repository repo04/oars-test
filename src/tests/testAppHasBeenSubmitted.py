#!/usr/bin/env python
from pages import LandingPage, PreviewPage


def test(args):
  #setup
  driver = args['driver']
  program_url = args['url']
  data = args['data']
  os = args['os']
  
  landing_page = LandingPage(driver, 'Login Page', program_url, os)
  try:
    landing_page.login(data)
  except Exception, e:
    pass

  #test
  preview_page = PreviewPage(landing_page.driver, 'Preview')
  preview_page.verify_application_submitted()