#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages

def test(args):
  landing_page = pages.LandingPage(args)
  landing_page.login()
  
  personal_info = pages.PersonalInformation(args)
  personal_info.auto_fill()

  prof_exp = pages.ProfessionalExperience(args)
  prof_exp.navigate_to()
  prof_exp.auto_fill()

  acad_background = pages.AcademicBackground(args)
  acad_background.navigate_to()
  acad_background.auto_fill()

  application_uploads = pages.ApplicationUploads(args)
  application_uploads.navigate_to()
  application_uploads.auto_fill()

  recommendations = pages.Recommendations(args)
  recommendations.navigate_to()
  recommendations.auto_fill()