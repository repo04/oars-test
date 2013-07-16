#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages

def test(args):
  landing_page = pages.LandingPage(args)
  landing_page.login()

  acad_background = pages.AcademicBackground(args)
  acad_background.navigate_to()
  acad_background.auto_fill()