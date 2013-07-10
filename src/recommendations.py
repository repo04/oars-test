import collections

def info():
  form = collections.OrderedDict()

  #format:
  #form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  #form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  #form['key (field name)'] = ['combo_box' , 'locator type (ID)', '(location)', '(to be selected)']
  #form['key (field name)'] = ['add_button' , 'locator type (link text)', '(link text)']
  #form['key (field name)'] = ['save_button' , 'locator type (index)', '(index)']

  #Recommendations
  form['request a recommendation'] = ['add_button' , 'link text', 'Request a recommendation']

  form['first name'] = ['text_box' , 'ID', 'id_recommenders.first_name', '(to be typed)']
  form['last name'] = ['text_box' , 'ID', 'id_recommenders.last_name', '(to be typed)']
  form['title'] = ['text_box' , 'ID', 'id_recommenders.job_title', '(to be typed)']
  form['employer'] = ['text_box' , 'ID', 'id_recommenders.employer', '(to be typed)']
  form['relationship to you'] = ['text_box' , 'ID', 'id_recommenders.relationship', '(to be typed)']
  form['address'] = ['text_box' , 'ID', 'id_recommenders.address_1', '(to be typed)']
  form['address2'] = ['text_box' , 'ID', 'id_recommenders.address_2', '(to be typed)']
  
  form['country'] = ['combo_box' , 'ID', 'id_recommenders.country', 'Kenya']

  form['city'] = ['text_box' , 'ID', 'id_recommenders.city', '(to be typed)']
  form['state'] = ['text_box' , 'ID', 'id_recommenders.state', '(to be typed)']
  form['zip code'] = ['text_box' , 'ID', 'id_recommenders.postal_code', '(to be typed)']
  form['email address'] = ['text_box' , 'ID', 'id_recommenders.email_address', '(to be typed)']
  form['confirm email address'] = ['text_box' , 'ID', 'id_recommenders_email_address_confirm', '(to be typed)']
  form['phone number'] = ['text_box' , 'ID', 'id_recommenders.phone_number', '(to be typed)']
  
  form['waive right to examine'] = ['combo_box' , 'ID', 'id_recommenders.is_waiving_examine_recommendation', 'Yes']
  
  form['key (field name)'] = ['save_button' , 'index', '0']
  
  return form