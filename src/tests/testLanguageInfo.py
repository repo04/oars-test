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
  language_info = landing_page.navigate_to('Language Information')
  data.auto_fill(language_info)