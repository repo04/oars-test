#!/usr/bin/env python
import sys
sys.path.insert(0, '../../src')
import pages
from selenium import webdriver

driver = webdriver.Firefox()


landing_page = pages.LandingPage(driver)
landing_page.login('https://au-mir-oars-sb01-qa.2u.com')
landing_page.teardown()


