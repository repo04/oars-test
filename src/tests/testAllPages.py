#!/usr/bin/env python
from pages import LandingPage


def test(args):
  #setup
  driver = args['driver']
  program_url = args['url']
  data = args['data']

  landing_page = LandingPage(driver, 'Login Page', program_url)
  landing_page.login(data)

  #test
  all_pages = landing_page.get_all_pages_from_navbar()
  
  for page in all_pages:
    page.navigate_to()
    data.auto_fill(page)
    page.save_and_continue()

  recommendations = landing_page.navigate_to('Recommendations')
  #needs two recommendations for a complete application
  data.auto_fill(recommendations)
  data.auto_fill(recommendations)
  recommendations.save_and_continue()

  preview_page = landing_page.preview_application()
  preview_page.continue_to_page()
  data.auto_fill(preview_page)
  preview_page.submit()
  preview_page.submit_with_offline_payment()
  preview_page.verify_application_submitted()