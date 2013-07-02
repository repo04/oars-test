#!/usr/bin/env python

from selenium import webdriver
import sys
sys.path.insert(0, '../../src')
import pages



driver = webdriver.Firefox()
landing_page = pages.LandingPage(driver)
landing_page.login('https://au-mir-oars-sb01-qa.2u.com')
landing_page.teardown()



