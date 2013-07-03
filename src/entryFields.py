import collections

def get_dictionary():
  
  elements = collections.OrderedDict() 

  #format:
  #elements['key'] = ['type' , 'locator type', 'location', 'user_action']

  #Personal Information
  elements['first name'] = ['text_box', 'ID' ,'id_first_name', 'Astudent1']
  elements['middle name'] = ['text_box', 'ID' ,'id_middle_name', 'nada']
  elements['last name'] = ['text_box', 'ID', 'id_last_name', 'Astudent2']
  
  elements['preferred name'] = ['radio_button', 'ID', 'id_has_preferred_name.yes', 'id_preferred_name'] 
  elements['alternate surname name'] = ['radio_button', 'ID', 'id_has_alternate_surname.yes', 'id_alternate_surname']
  
  elements['birthdate'] = ['text_box', 'ID' ,'id_birthdate', '01/29/1990']
  
  elements['gender'] = ['radio_button', 'ID', 'id_gender.male', '']
  
  elements['birthplace'] = ['combo_box', 'ID', 'id_birthplace.country', 'United States']
  elements['country of citizenship'] = ['combo_box', 'ID', 'id_primary_country_of_citizenship', 'United States']
  elements['social security number'] = ['text_box', 'ID', 'id_social_security_number', '123-45-6789']

  #Plans for Graduate Study
  elements['preferred enrollment date'] = ['combo_box', 'ID', 'id_program_start_date', 'May 2014']
  elements['preferred enrollment status'] = ['combo_box', 'ID', 'id_full_or_part_time', 'Full-time']
  elements['previously applied year'] = ['radio_button', 'ID', 'id_has_previously_applied.yes', 'id_previously_applied_year']
  elements['learned about program'] = ['combo_box', 'ID', 'id_learned_about_program', 'Other'] #ID = id_learned_about_program_other 
  elements['other graduate programs'] = ['combo_box', 'ID', 'id_is_applying_other_graduate_programs', 'Yes'] #class = button action medium add + class = button action medium save
  
  #Background Information
  elements['native language'] = ['radio_button', 'ID', 'id_is_native_english_speaker.no', 'id_native_language']
  elements['undergrad degree country'] = ['radio_button', 'ID', 'id_has_undergrad_degree_from_english_country.yes', 'id_undergrad_degree_country']
  elements['post grad degree country'] = ['radio_button', 'ID', 'id_has_grad_degree_from_english_country.yes', 'id_grad_degree_country']

  #elements[''] "add a language" button
  elements['international experience'] = ['combo_box', 'ID', 'id_international_experience', 'Other'] #id_international_experience_other

  #Other Information
  elements['peace corps'] = ['radio_button', 'ID', 'id_is_peace_corps_or_tfa.yes', 'id_peace_corps_or_tfa']
  elements['us military'] = ['radio_button', 'ID', 'id_is_military_active_or_veteran.yes', ''] #text popup
  elements['first gen college student'] = ['radio_button', 'ID', 'id_is_first_gen_college_student.yes', ''] #text popup
  
  #Contact Information
  elements['email address'] = ['text_box', 'ID', 'id_email_address', 'ogriffin+oars1@2u.com']
  elements['email address confirm'] = ['text_box', 'ID', 'id_email_address_confirm', 'ogriffin+oars1@2u.com']
  elements['street address'] = ['text_box', 'ID', 'id_address.primary.address_1', '4 Privet Drive']
  
  elements['country'] = ['combo_box', 'ID', 'id_address.primary.country', 'India']

  elements['city'] = ['text_box', 'ID', 'id_address.primary.city', 'Little Whinging']
  elements['state'] = ['text_box', 'ID', 'id_address.primary.state', 'Maharashtra'] #changes to combo box if primary country is US
  elements['zip code'] = ['text_box', 'ID', 'id_address.primary.postal_code', '10011']

  elements['secondary address'] = ['radio_button', 'ID', 'id_secondary_address.yes', ''] # multiple text fields appear
  
  elements['which address'] = ['combo_box', 'ID', 'id_will_reside_at_address', 'Secondary']

  elements['home phone country'] = ['combo_box', 'ID', 'id_phone.home.country', 'United States(+1)']
  elements['home phone number'] = ['text_box', 'ID', 'id_phone.home', '555-123-4567']

  elements['mobile mobile country'] = ['combo_box', 'ID', 'id_phone.mobile.country', 'United States (+1)']
  elements['mobile mobile number'] = ['text_box', 'ID', 'id_phone.mobile', '555-891-0111']

  elements['work phone country'] = ['combo_box', 'ID', 'id_phone.work.country', 'United States (+1)']
  elements['work phone number'] = ['text_box', 'ID', 'id_phone.work', '555-213-1415']

  #Race and Ethnicity Information
  elements['peace corps'] = ['radio_button', 'ID', 'id_is_hispanic_or_latino.no', '']
  elements[''] = ['', '', '', ''] #race checkbox

  return elements