from faker import Faker
import random, decimal, os, userNames, string

#inherits from Faker - used to generate fake data
class FakeData(Faker):

  firstname = None
  lastname = None
  gmail = None #used for logging into gmail
  email = None #used for logging into site
  #new_email = None #used for new user creation
  password = None
  path_to_test_doc = None #used for file uploads
  login_info = None

  def __init__(self):
    super(FakeData, self).__init__()
    
    self.firstname = self.first_name()
    self.lastname = self.last_name()
    
    self.login_info = userNames.LoginInfo() #used for storing usernames/passwords

    self.gmail = self.login_info.get_login_info('gmail') #method from userNames.py
    self.email = self.login_info.get_login_info('email') #method from userNames.py
    #self.new_email = u.get_login_info('new_email')
    self.password = self.login_info.get_login_info('password') #method from userNames.py

    #self.path_to_test_doc = os.path.abspath('test_doc.pdf')
    self.path_to_test_doc = os.path.abspath('./test_doc.pdf')
    
  def create_random_username(self):
    self.login_info.random_username()
    self.email = self.login_info.get_login_info('email')

  def _fake_date(self, element):
    date_format = element.get_attribute('class')
    year = random.choice(range(1950, 2000))
    month = random.choice(range(1, 12))
    day = random.choice(range(1, 27))
    
    try:
      if element.find_element_by_xpath("following-sibling::small[position()=1]").text=='YYYY':
          return year
    except Exception, e:
      pass

    if 'mm-yyyy' in date_format:
      return str(month)+'/'+str(year)
    else:
      return str(month)+'/'+str(day)+'/'+str(year)

  def _fake_name(self, element_id):
    if 'first' in element_id:
      return self.firstname
    elif 'middle' in element_id:
      return random.choice(string.letters)
    elif 'last' in element_id and 'name' in element_id:
      return self.lastname
    elif 'preferred' in element_id:
      return self.name()
    elif 'alternate' in element_id:
      return self.last_name()
    elif 'signature' in element_id:
      return self.firstname+' '+self.lastname
    else:
      return self.name()

  def _fake_phone(self, element_id):
    num1 = random.choice(range(100, 1000))
    num2 = random.choice(range(1000, 10000))
    return str(num1)+'-'+'555'+'-'+str(num2)

  def _fake_address(self, element_id):
    if '1' in element_id:
      return self.street_address()
    else: 
      return 'Suite 7B'

  def _get_score(self, element):
    try:
      score_range_text = element.find_element_by_xpath("following-sibling::small[position()=1]").text
      score_range = score_range_text.split("-")
      lower_bound = int(float(score_range[0]))
      upper_bound = int(float(score_range[1]))
      return random.choice(range(lower_bound, upper_bound))
    except Exception, e:
      return random.choice(range(0, 30))

  def fill_valid_value(self, element):
    element_id = element.get_attribute('id')
    element_class = element.get_attribute('class')
    
    if 'signature' in element_id:
      if 'date' in element_id:
        return self._fake_date(element)
      else:
        return self._fake_name(element.get_attribute('id'))
    elif 'employees' in element_id or 'salary' in element_id or 'bonus' in element_id or 'commission' in element_id:
      return random.choice(range(10000, 100000))
    elif 'initial' in element_id:
      return 'J'
    elif 'total' in element_id and 'years' in element_id or 'months' in element_id:
      return random.choice(range(1, 10))
    elif 'name' in element_id:
      if 'test' in element_id:
        return 'a test name'
      else:
        return self._fake_name(element_id)
    elif 'address' in element_id and 'years' in element_id:
      return random.choice(range(0, 20))
    elif '.address' in element_id:
      return self._fake_address(element_id)
    elif 'city' in element_id or 'state' in element_id:
      return self.city()
    elif 'postal' in element_id or 'zip' in element_id:
      return self.zip_code()
    elif 'date' in element_id or 'date' in element_class:
      return self._fake_date(element)
    elif 'year' in element_id:
      return random.choice(range(1950, 2000))
    elif 'company' in element_id or 'employer' in element_id:
      return self.company()
    elif 'email' in element_id:
      return self.email
    elif 'phone' in element_id:
      return self._fake_phone(element.get_attribute('id'))
    elif 'security' in element_id or 'ssn' in element_id:
      if 'format' in element.find_element_by_xpath("following-sibling::small[position()=1]").text:
        return '123456789'
      else:
        return '123-45-6789'
    elif 'university' in element_id:
      return self.city()+' University'
    elif 'language' in element_id:
      return 'Latin'
    elif 'score' in element_id:
      if 'gmat' in element_id or 'gre' in element_id or 'toefl' in element_id or 'ielts' in element_id:
        return self._get_score(element)
      else:
        return random.choice(range(400,600))
    elif 'gpa' in element_id:
      return str(decimal.Decimal(random.randrange(41))/decimal.Decimal(10))
    elif 'account_number' in element_id: #fake payment info
      return 4111111111111111
    elif 'expires' in element_id: #fake payment info
      return '12/2020'
    elif 'cvv' in element_id:
      return 123
    else:
      return 'giggity'