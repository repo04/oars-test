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
  community_standards = landing_page.navigate_to('Community Standards')
  data.auto_fill(community_standards)