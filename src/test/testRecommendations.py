#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages

def test(args):
  landing_page = pages.LandingPage(args)
  landing_page.login()

  recommendations = pages.Recommendations(args)
  recommendations.navigate_to()
  recommendations.auto_fill()