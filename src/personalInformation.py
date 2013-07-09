import collections

def info():

  form = collections.OrderedDict() 

  #format:
  #form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  #form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)']
  #form['key (field name)'] = ['combo_box' , 'locator type (ID)', '(location)', '(to be selected)']
  #form['key (field name)'] = ['add_button' , 'locator type (link text)', '(location)']
  #form['key (field name)'] = ['save_button' , 'locator type (index)', '(location)']

  #Personal Information
  form['first name'] = ['text_box', 'ID' ,'id_first_name', 'Astudent1']
  form['middle name'] = ['text_box', 'ID' ,'id_middle_name', 'nada']
  form['last name'] = ['text_box', 'ID', 'id_last_name', 'Astudent2']
  
  form['preferred name'] = ['radio_button', 'ID', 'id_has_preferred_name.yes', 'id_preferred_name'] 
  form['alternate surname name'] = ['radio_button', 'ID', 'id_has_alternate_surname.yes', 'id_alternate_surname']
  
  form['birthdate'] = ['text_box', 'ID','id_birthdate', '01/29/1990']
  
  form['gender'] = ['radio_button', 'ID', 'id_gender.male', '']
  
  form['birthplace'] = ['combo_box', 'ID', 'id_birthplace.country', 'United States']
  form['country of citizenship'] = ['combo_box', 'ID', 'id_primary_country_of_citizenship', 'United States']
  form['social security number'] = ['text_box', 'ID', 'id_social_security_number', '123-45-6789']

  #Plans for Graduate Study
  form['preferred enrollment date'] = ['combo_box', 'ID', 'id_program_start_date', 'May 2014']
  form['preferred enrollment status'] = ['combo_box', 'ID', 'id_full_or_part_time', 'Full-time']
  form['previously applied year'] = ['radio_button', 'ID', 'id_has_previously_applied.yes', 'id_previously_applied_year']
  form['learned about program'] = ['combo_box', 'ID', 'id_learned_about_program', 'Search Engine/Online Ad']
  form['other graduate programs'] = ['combo_box', 'ID', 'id_is_applying_other_graduate_programs', 'Yes']
  
  form['add a program'] = ['add_button', 'link text', 'Add a program']
  form['university'] = ['text_box' , 'ID', 'id_other_graduate_programs.university', 'Test School'] 
  form['program'] = ['text_box', 'ID', 'id_other_graduate_programs.program', 'Test Prog']
  form['save university'] = ['save_button', 'index', '0']
  
  #Background Information
  form['native language'] = ['radio_button', 'ID', 'id_is_native_english_speaker.no', 'id_native_language']
  form['undergrad degree country'] = ['radio_button', 'ID', 'id_has_undergrad_degree_from_english_country.yes', 'id_undergrad_degree_country']
  form['post grad degree country'] = ['radio_button', 'ID', 'id_has_grad_degree_from_english_country.yes', 'id_grad_degree_country']
  
  form['add a language'] = ['add_button', 'link text', 'Add a language']
  form['language'] = ['text_box', 'ID','id_other_languages.language', 'Parsel Tongue']
  form['proficiency'] = ['combo_box', 'ID', 'id_other_languages.proficiency', 'Advanced']
  form['save language'] = ['save_button', 'index', '1']
  
  form['international experience'] = ['combo_box', 'ID', 'id_international_experience', 'Study Abroad'] #id_international_experience_other

  #Other Information
  form['peace corps'] = ['radio_button', 'ID', 'id_is_peace_corps_or_tfa.yes', 'id_peace_corps_or_tfa']
  form['us military'] = ['radio_button', 'ID', 'id_is_military_active_or_veteran.yes', ''] #text popup
  form['first gen college student'] = ['radio_button', 'ID', 'id_is_first_gen_college_student.yes', ''] #text popup
  
  #Contact Information
  form['email address'] = ['text_box', 'ID', 'id_email_address', 'ogriffin+oars1@2u.com']
  form['email address confirm'] = ['text_box', 'ID', 'id_email_address_confirm', 'ogriffin+oars1@2u.com']
  form['street address'] = ['text_box', 'ID', 'id_address.primary.address_1', '4 Privet Drive']
  
  form['country'] = ['combo_box', 'ID', 'id_address.primary.country', 'India']

  form['city'] = ['text_box', 'ID', 'id_address.primary.city', 'Little Whinging']
  form['state'] = ['text_box', 'ID', 'id_address.primary.state', 'Maharashtra'] #changes to combo box if primary country is US
  form['zip code'] = ['text_box', 'ID', 'id_address.primary.postal_code', '10011']

  form['secondary address'] = ['radio_button', 'ID', 'id_secondary_address.no', ''] # multiple text fields appear if yes
  
  form['which address'] = ['combo_box', 'ID', 'id_will_reside_at_address', 'Home / Primary']

  form['home phone country'] = ['combo_box', 'ID', 'id_phone.home_country', 'United States (+1)']
  form['home phone number'] = ['text_box', 'ID', 'id_phone.home', '555-123-home']

  form['mobile mobile country'] = ['combo_box', 'ID', 'id_phone.mobile_country', 'United States (+1)']
  form['mobile mobile number'] = ['text_box', 'ID', 'id_phone.mobile', '555-123-mobi']

  form['work phone country'] = ['combo_box', 'ID', 'id_phone.work_country', 'United States (+1)']
  form['work phone number'] = ['text_box', 'ID', 'id_phone.work', '555-123-work']

  #Race and Ethnicity Information
  form['is hispanic or latino'] = ['radio_button', 'ID', 'id_is_hispanic_or_latino.no', '']
  form[''] = ['', '', '', ''] #race checkbox

  return form