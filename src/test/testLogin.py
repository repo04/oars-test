#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages

def test_login(args):
  landing_page = pages.LandingPage(args)
  landing_page.login(args['url'])
  landing_page.teardown()