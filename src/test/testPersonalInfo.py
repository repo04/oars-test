#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages, fillData

def test(args):
  #setup
  landing_page = pages.LandingPage(args)
  landing_page.login()
  f=fillData.Filler()

  personal_info = pages.PersonalInformation(args)
  
  #test
  f.auto_fill(personal_info)