from faker import Faker
import random

#uses data to generate fake info
class FakeData(object):

  faker = None

  def __init__(self):
    self.faker = Faker()
		
  def _fake_date(self, date_format):
    year = random.choice(range(1950, 2013))
    month = random.choice(range(0, 13))
    day = random.choice(range(0, 29))

    if 'mm-dd-yyyy' in date_format:
      return str(month)+'/'+str(day)+'/'+str(year)
    elif 'mm-yyyy' in date_format:
      return str(month)+'/'+str(year)

  def _fake_name(self, element_id):
    if 'first' in element_id or 'middle' in element_id:
      return self.faker.first_name()
    elif 'last' in element_id and 'name' in element_id:
      return self.faker.last_name()
    elif 'preferred' in element_id:
      return self.faker.name()
    elif 'alternate' in element_id:
      return self.faker.last_name()

  def _fake_phone(self, element_id):
    num1 = random.choice(range(100,1000))
    num2 = random.choice(range(1000,10000))
    return str(num1)+'-'+'555'+'-'+str(num2)

  def fill_valid_value(self, element):
    element_id = element.get_attribute('id')
    
    if 'name' in element_id:
      return self._fake_name(element.get_attribute('id'))
    elif '.address' in element_id:
      return self.faker.street_address()
    elif 'city' in element_id:
      return self.faker.city()
    elif 'postal' in element_id:
      return self.faker.zip_code()
    elif 'date' in element_id:
      return self._fake_date(element.get_attribute('class'))
    elif 'company' in element_id or 'employer' in element_id:
      return self.faker.company()
    elif 'email' in element_id:
      return self.faker.email()
    elif 'phone' in element_id:
      return self._fake_phone(element.get_attribute('id'))
    elif 'security' in element_id:
      return '123-45-6789'
    else:
      return 'filler-value'