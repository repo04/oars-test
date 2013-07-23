#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages, fillData

def test(args):
  #setup
  landing_page = pages.LandingPage(args)
  landing_page.create_user()
  f=fillData.Filler()
  
  #these pages needed to be instantiated after logging in or else error occurs
  personal_info = pages.PersonalInformation(args)
  prof_exp = pages.ProfessionalExperience(args)
  acad_background = pages.AcademicBackground(args)
  application_uploads = pages.ApplicationUploads(args)
  recommendations = pages.Recommendations(args)

  #test
  f.auto_fill(personal_info)
  
  prof_exp.navigate_to()
  f.auto_fill(prof_exp)

  acad_background.navigate_to()
  f.auto_fill(acad_background)

  application_uploads.navigate_to()
  f.auto_fill(application_uploads)

  recommendations.navigate_to()
  f.auto_fill(recommendations)