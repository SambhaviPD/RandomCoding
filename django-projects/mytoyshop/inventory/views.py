from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (CreateView, UpdateView, ListView, DetailView)

from . import models

# Create your views here.
class AddCategory(SuccessMessageMixin, CreateView):
	model = models.Category
	fields = '__all__'
	success_message = 'Category added successfully.'

class UpdateCategory(SuccessMessageMixin, UpdateView):
	model = models.Category
	fields = '__all__'
	success_message = 'Category updated successfully.'

class ListCategory(ListView):
	model = models.Category
	queryset = models.Category.objects.all()
	context_object_name = 'categories'
	paginate_by = 10

