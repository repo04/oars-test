#!/usr/bin/env python
from pages import LandingPage


def test(args):
  #setup
  driver = args['driver']
  program_url = args['url']
  data = args['data']
  os = args['os']

  landing_page = LandingPage(driver, 'Login Page', program_url, os)
  landing_page.login(data)

  #test
  clinical_experience = landing_page.navigate_to('Clinical Experience')
  data.auto_fill(clinical_experience)