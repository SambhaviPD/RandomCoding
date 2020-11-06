from django import urls
from django.contrib.auth.models import Group, User
from django.contrib.messages import get_messages

import pytest

from inventory import models

@pytest.fixture
def group_billingadmin(db) -> Group:
	group, created = Group.objects.get_or_create(name='billingadmin')
	return group

@pytest.fixture
def test_create_user(db, group_billingadmin: Group) -> None:
	user = User.objects.create_user('Sam')
	user.groups.add(group_billingadmin)
	return user

# def test_billingadmin_users(db):
# 	users = User.objects.filter(groups__name='shopadmin')
# 	assert len(users) == 1

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

@pytest.fixture
def category_softtoys(db) -> models.Category:
	category = models.Category.objects.get_or_create( \
		id=1, \
		name='Soft Toys', \
		description='Fluffy toys for toddlers'
		)
	return category

@pytest.mark.django_db
def test_create_toy(client, category_softtoys):
	add_toy_url = urls.reverse('inventory:add_toy')
	resp = client.post(add_toy_url, {
			'id': 1,
			'name': 'Rabbit with carrot stuffed soft plush toy',
			'category': category_softtoys,
			'description': 'Cute soft toy',
			'cost':194.00,
			'brand':'Deals India',
			'activity_type': 'Indoor'
		})
	assert resp.status_code == 200
	assert 'Add/Update details about a Toy' in str(resp.content)
	#messages = [m.message for m in get_messages(resp.wsgi_request)]
	#assert 'Toy added successfully' in messages

@pytest.mark.django_db
def test_create_category_without_name(client):
	add_category_url = urls.reverse('inventory:add_category')
	resp = client.post(add_category_url, {
			'id':1, 
			'description':'Fluffy toys for toddlers'
		})
	assert resp.status_code == 200
	assert b'This field is required' in resp.content