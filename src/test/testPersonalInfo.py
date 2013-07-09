#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages

def test(args):
  landing_page = pages.LandingPage(args)
  landing_page.login()
  
  #personal_info = pages.PersonalInformation(args)
  #personal_info.complete()

  #pro_exp = pages.ProfessionalExperience(args)
  #pro_exp.navigate_to()
  #pro_exp.complete()
  #pro_exp.save_and_signout()
  #pro_exp.teardown()

  acad_background = pages.AcademicBackground(args)
  acad_background.navigate_to()
  acad_background.complete()