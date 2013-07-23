#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages, fillData

def test(args):
  #setup
  landing_page = pages.LandingPage(args)
  landing_page.login()
  f=fillData.Filler()

  acad_background = pages.AcademicBackground(args)
  
  #test
  acad_background.navigate_to()
  f.auto_fill(acad_background)