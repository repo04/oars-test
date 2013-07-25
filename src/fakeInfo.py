from faker import Faker
import random, decimal, os

#inherits from Faker. used to generate fake data.
class FakeData(Faker):

  firstname = None
  lastname = None
  email = None
  new_email = None
  password = None
  path_to_test_doc = None

  def __init__(self):
    super(FakeData, self).__init__()
    
    self.firstname = self.first_name()
    self.lastname = self.last_name()
    self.email = 'oars.tests@2u.com'
    self.new_email = 'oars.tests+'+str(random.choice(range(100, 1000)))+'@2u.com'
    self.password = 'Moodle1!'

    self.path_to_test_doc = os.path.abspath('test_doc.pdf')
    
  def _fake_date(self, date_format):
    year = random.choice(range(1950, 2000))
    month = random.choice(range(1, 12))
    day = random.choice(range(1, 30))

    if 'mm-yyyy' in date_format:
      return str(month)+'/'+str(year)
    else:
      return str(month)+'/'+str(day)+'/'+str(year)

  def _fake_name(self, element_id):
    if 'first' in element_id:
      return self.firstname
    elif 'middle' in element_id:
      return ''
    elif 'last' in element_id and 'name' in element_id:
      return self.lastname
    elif 'preferred' in element_id:
      return self.name()
    elif 'alternate' in element_id:
      return self.last_name()
    elif 'signature' in element_id:
      return self.firstname, self.lastname

  def _fake_phone(self, element_id):
    num1 = random.choice(range(100, 1000))
    num2 = random.choice(range(1000, 10000))
    return str(num1)+'-'+'555'+'-'+str(num2)

  def _fake_address(self, element_id):
    if '1' in element_id:
      return self.street_address()
    else: 
      return 'Suite 7B'

  def fill_valid_value(self, element):
    element_id = element.get_attribute('id')
    
    if 'signature' in element_id:
      if 'date' in element_id:
        return self._fake_date(element.get_attribute('class'))
      else:
        return self._fake_name(element.get_attribute('id'))
    elif 'name' in element_id:
      return self._fake_name(element.get_attribute('id'))
    elif '.address' in element_id:
      return self._fake_address(element_id)
    elif 'city' in element_id:
      return self.city()
    elif 'postal' in element_id:
      return self.zip_code()
    elif 'date' in element_id:
      return self._fake_date(element.get_attribute('class'))
    elif 'year' in element_id:
      return random.choice(range(1950, 2000))
    elif 'company' in element_id or 'employer' in element_id:
      return self.company()
    elif 'email' in element_id:
      return self.email
    elif 'phone' in element_id:
      return self._fake_phone(element.get_attribute('id'))
    elif 'security' in element_id:
      return '123-45-6789'
    elif 'university' in element_id:
      return self.city()+' University'
    elif 'language' in element_id:
      return 'Latin'
    elif 'score' in element_id:
      return random.choice(range(100,800))
    elif 'gpa' in element_id:
      return str(decimal.Decimal(random.randrange(41))/decimal.Decimal(10))
    else:
      return 'filler-value'