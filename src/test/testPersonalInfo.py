#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages

def test(args):
  landing_page = pages.LandingPage(args)
  landing_page.login()
  
  personal_info = pages.PersonalInformation(args)
  personal_info.auto_fill()