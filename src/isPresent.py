from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IsPresent(object):

  wait = None

  def __init__(self, driver):
    self.wait = WebDriverWait(driver, 20)

###########################################################################################
  def is_element_clickable_by_class_name(self, class_name):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))

  def is_element_clickable_by_css_selector(self, css_selector):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

  def is_element_clickable_by_id(self, id):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.ID, id)))

  def is_element_clickable_by_link_text(self, link_text):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))

  def is_element_clickable_by_name(self, name):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.NAME, name)))

  def is_element_clickable_by_partial_link_text(self, partial_link_text):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, partial_link_text)))

  def is_element_clickable_by_tag_name(self, tag_name):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, tag_name)))

  def is_element_clickable_by_xpath(self, xpath):
    wait_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

###########################################################################################
  def is_text_present_by_class_name(self, class_name, text):
    wait_element = self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, class_name), text))

  def is_text_present_by_css_selector(self, css_selector, text):
    wait_element = self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), text))

  def is_text_present_by_id(self, id, text):
    wait_element = self.wait.until(EC.text_to_be_present_in_element((By.ID, id), text))

  def is_text_present_by_link_text(self, link_text, text):
    wait_element = self.wait.until(EC.text_to_be_present_in_element((By.LINK_TEXT, link_text), text))

  def is_text_present_by_name(self, name, text):
    wait_element = self.wait.until(EC.text_to_be_present_in_element((By.NAME, name), text))

  def is_text_present_by_partial_link_text(self, link_text, text):
    wait_element = self.wait.until(EC.text_to_be_present_in_element((By.PARTIAL_LINK_TEXT, partial_link_text), text))

  def is_text_present_by_tag_name(self, name, text):
    wait_element = self.wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, tag_name), text))    

  def is_text_present_by_xpath(self, xpath, text):
    wait_element = self.wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))

###########################################################################################
  def is_element_visible(self, element):
    wait_element = self.wait.until(EC.visibility_of(element))

  def title_contains(self, text):
    wait_element = self.wait.until(EC.title_contains(text))

    '''presence_of_element_located(locator)

    text_to_be_present_in_element(locator, text_)

    visibility_of_element_located(locator)

    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Continue')))'''