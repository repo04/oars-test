#!/usr/bin/env python
from pages import LandingPage


def test(args):
  #setup
  driver = args['driver']
  program_url = args['url']
  data = args['data']

  landing_page = LandingPage(driver, 'Login Page', program_url)

  #test
  landing_page.login(data)
