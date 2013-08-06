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
  code_of_conduct = landing_page.navigate_to('Code Of Conduct')
  data.auto_fill(code_of_conduct)