#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages

def test(args):
  landing_page = pages.LandingPage(args)
  landing_page.login()

  prof_exp = pages.ProfessionalExperience(args)
  prof_exp.navigate_to()
  prof_exp.auto_fill()