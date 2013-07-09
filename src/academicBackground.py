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
  form['upload transcript'] = ['attach_a_file', 'name', 'file', '/Users/ogriffin/Desktop/test_doc.txt']
  
  return form

  '''
  form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  form['key (field name)'] = ['combo_box' , 'locator type (ID)', '(location)', '(to be selected)']
  form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  form['key (field name)'] = ['combo_box' , 'locator type (ID)', '(location)', '(to be selected)']
  form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  
  #MAJOR BOX/SPECIAL TREATMENT?

  form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  form['key (field name)'] = ['text_box' , 'locator type (ID)', '(location)', '(to be typed)']
  '''
'''
  form['key (field name)'] = ['save_button' , 'locator type (index)', '(index)']
  



  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
  form['key (field name)'] = ['radio_button' , 'locator type (ID)', '(location)', '(id of node or '')']
'''