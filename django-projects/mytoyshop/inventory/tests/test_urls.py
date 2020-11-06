from django.urls import reverse, resolve

def test_addcategory_url():
	path = reverse('inventory:add_category')
	assert resolve(path).view_name == 'inventory:add_category'

def test_addtoy_url():
	path = reverse('inventory:add_toy')
	assert resolve(path).view_name == 'inventory:add_toy'