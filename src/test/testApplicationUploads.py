#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import pages

def test(args):
  landing_page = pages.LandingPage(args)
  landing_page.login()

  application_uploads = pages.ApplicationUploads(args)
  application_uploads.navigate_to()
  application_uploads.auto_fill()