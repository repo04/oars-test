#!/usr/bin/env python
from pageObject import Page as page

class LandingPage(page):
  def __init__(self, args):
    # initialize parent class
    super(LandingPage, self).__init__(args)

class PersonalInformation(page):
  def __init__(self, args):
    super(PersonalInformation, self).__init__(args, 0)
    
class ProfessionalExperience(page):
  def __init__(self, args):
    super(ProfessionalExperience, self).__init__(args, 1)
  
class AcademicBackground(page):
  def __init__(self, args):
    super(AcademicBackground, self).__init__(args, 2)
    
class ApplicationUploads(page):
  def __init__(self, args):
    super(ApplicationUploads, self).__init__(args, 3)

class Recommendations(page):
  def __init__(self, args):
    super(Recommendations, self).__init__(args, 4)
