import collections

def info():
  form = collections.OrderedDict()

  #format:
  #form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  #form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  #form['key (field name)'] = ['combo_box' , 'locator type (ID)', '(location)', '(to be selected)']
  #form['key (field name)'] = ['add_button' , 'locator type (link text)', '(link text)']
  #form['key (field name)'] = ['save_button' , 'locator type (index)', '(index)']

  #Professional Experience
  form['how many years of experience'] = ['combo_box' , 'ID', 'id_full_time_experience', '2-3 Years']
  
  form['add a position'] = ['add_button' , 'link text', 'Add a position']
  
  form['employer name'] = ['text_box' , 'ID', 'id_employment.company', '2U']
  form['job title'] = ['text_box' , 'ID', 'id_employment.position', 'intern']
  form['start date'] = ['text_box' , 'ID', 'id_employment.start_date', '01/2012']
  form['end date'] = ['text_box' , 'ID', 'id_employment.end_date', '12/2012']
  
  form['employment status'] = ['combo_box' , 'ID', 'id_employment.status', 'Full time']
  
  form['currently works here'] = ['radio_button' , 'ID', 'id_employment.currently_works_here.yes', '']
  
  form['employment country'] = ['combo_box' , 'ID', 'id_employment.country', 'Albania']
  
  form['employment state'] = ['text_box' , 'ID', 'id_employment.state', ' New York']
  
  form['save position'] = ['save_button' , 'index', '0']

  return form
