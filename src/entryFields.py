import collections

def get_dictionary():
  
  elements = collections.OrderedDict() 

  #format:
  #elements['key'] = ['type' , 'locator type', 'location', 'user_action']

  elements['first name'] = ['text_box', 'ID' ,'id_first_name', 'Astudent1']
  elements['middle name'] = ['text_box', 'ID' ,'id_middle_name', 'nada']
  elements['last name'] = ['text_box', 'ID', 'id_last_name', 'Astudent2']
  
  elements['preferred name'] = ['radio_button', 'ID', {'yes': 'id_has_preferred_name.yes', 'no': 'id_has_preferred_name.no'}, 'id_preferred_name'] 
  elements['alternate surname name'] = ['radio_button', 'ID', {'yes': 'id_has_alternate_surname.yes', 'no': 'id_has_alternate_surname.no'}, 'id_alternate_surname']
  
  elements['birthdate'] = ['text_box', 'ID' ,'id_birthdate', '01/29/1990']
  
  elements['gender'] = ['radio_button', 'ID', {'yes': 'id_gender.male','no': 'id_gender.female'}, '']
  
  elements['birthplace'] = ['combo_box', 'ID', 'id_birthplace.country', 'India']
  elements['country of citizenship'] = ['', '', '', '']
  elements['social security number'] = ['', '', '', '']
  
  return elements