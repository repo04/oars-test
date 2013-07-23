#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages, fillData

def test(args):
  #setup
  landing_page = pages.LandingPage(args)
  landing_page.login()
  f=fillData.Filler()

  application_uploads = pages.ApplicationUploads(args)
  
  #test
  application_uploads.navigate_to()
  f.auto_fill(application_uploads)