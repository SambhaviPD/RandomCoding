from django import urls
import pytest

@pytest.mark.django_db
def test_create_category(client):
	add_category_url = urls.reverse('inventory:add_category')
	resp = client.post(add_category_url, {
			'id':1, 
			'name':'Soft Toys', 
			'description':'Fluffy toys for toddlers'
		})
	assert resp.status_code == 302
	assert resp.url.startswith(urls.reverse('inventory:update_category', kwargs={'pk':1}))

@pytest.mark.django_db
def test_create_category_without_name(client):
	add_category_url = urls.reverse('inventory:add_category')
	resp = client.post(add_category_url, {
			'id':1, 
			'description':'Fluffy toys for toddlers'
		})
	assert resp.status_code == 200
	assert b'name' in resp.content