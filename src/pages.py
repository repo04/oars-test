#!/usr/bin/env python
from pageObject import Page as page

class LandingPage(page):
  def __init__(self, driver):
    # initialize parent class
    super(LandingPage, self).__init__(driver)

class PersonalInformation(page):
  def __init__(self, driver):
    super(PersonalInformation, self).__init__(driver)
    
  def navigateTo(self):
    self.elements[0].click()

class ProfessionalExperience(page):
  def __init__(self, driver):
    super(ProfessionalExperience, self).__init__(driver)
    
  def navigateTo(self):
    self.elements[1].click()

class AcademicBackground(page):
  def __init__(self, driver):
    super(AcademicBackground, self).__init__(driver)
    
  def navigateTo(self):
    self.elements[2].click()

class ApplicationUploads(page):
  def __init__(self, driver):
    super(ApplicationUploads, self).__init__(driver)
    
  def navigateTo(self):
    self.elements[3].click()

class Recommendations(page):
  def __init__(self, driver):
    super(Recommendations, self).__init__(driver)
    
  def navigateTo(self):
    self.elements[4].click()