#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages, fillData

def test(args):
  #setup
  landing_page = pages.LandingPage(args)
  landing_page.login()
  f=fillData.Filler()

  recommendations = pages.Recommendations(args)
  
  #test
  recommendations.navigate_to()
  f.auto_fill(recommendations)
  recommendations.teardown()