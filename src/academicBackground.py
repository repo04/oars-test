import collections

def info():
  form = collections.OrderedDict()

  #format:
  #form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  #form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  #form['key (field name)'] = ['combo_box' , 'locator type (ID)', '(location)', '(to be selected)']
  #form['key (field name)'] = ['add_button' , 'locator type (link text)', '(link text)']
  #form['key (field name)'] = ['save_button' , 'locator type (index)', '(index)']

  #Academic Background
  form['add a college'] = ['add_button' , 'link text', 'Add a college']
  
  form['college name'] = ['text_box' , 'locator type (ID)', 'id_colleges.', '(to be typed)']
  form['college country'] = ['combo_box' , 'locator type (ID)', 'id_colleges.', '(to be selected)']
  form['college state'] = ['text_box' , 'locator type (ID)', 'id_colleges.', '(to be typed)']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', 'id_colleges.', '(id of node or '')']
  form['year started'] = ['text_box' , 'locator type (ID)', 'id_colleges.', '(to be typed)']
  form['year ended'] = ['text_box' , 'locator type (ID)', 'id_colleges.', '(to be typed)']
  form['expected graduation'] = ['text_box' , 'locator type (ID)', 'id_colleges.', '(to be typed)'] #dynamic fields
  form['key (field name)'] = ['combo_box' , 'locator type (ID)', 'id_colleges.', '(to be selected)']
  form['key (field name)'] = ['text_box' , 'locator type (ID)', 'id_colleges.', '(to be typed)']
  
  #MAJOR BOX/SPECIAL TREATMENT?

  form['key (field name)'] = ['text_box' , 'locator type (ID)', 'id_colleges.', '(to be typed)']
  form['key (field name)'] = ['text_box' , 'locator type (ID)', 'id_colleges.', '(to be typed)']

  #form['upload transcript'] = ['attach_a_file', 'name', 'file', '/Users/ogriffin/Desktop/test_doc.txt']

  form['key (field name)'] = ['save_button' , 'locator type (index)', '(index)']


  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']

  return form