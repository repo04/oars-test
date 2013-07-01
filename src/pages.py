#!/usr/bin/env python
from pageObject import Page as page

class LandingPage(page):
  def __init__(self, driver):
    # initialize parent class
    super(LandingPage, self).__init__(driver)

class PersonalInformation(page):
  def __init__(self, driver):
    super(PersonalInformation, self).__init__(driver)
    
class ProfessionalExperience(page):
  def __init__(self, driver):
    super(ProfessionalExperience, self).__init__(driver)
    
class AcademicBackground(page):
  def __init__(self, driver):
    super(AcademicBackground, self).__init__(driver)
    
class ApplicationUploads(page):
  def __init__(self, driver):
    super(ApplicationUploads, self).__init__(driver)

class Recommendations(page):
  def __init__(self, driver):
    super(Recommendations, self).__init__(driver)
