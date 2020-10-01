from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DetailView)
from django.views.generic.base import RedirectView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from . import models

# Create your views here.
class RedirectStudent(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		try:
			student = models.Student.objects.get(id=kwargs['pk'])
			return reverse('student:update_student', \
				kwargs={'pk':student.id})
		except ObjectDoesNotExist:
			return reverse('student:add_student')

class AddStudent(SuccessMessageMixin, CreateView):
    model = models.Student
    fields = '__all__'
    success_message = 'Student details added successfully'

class UpdateStudent(SuccessMessageMixin, UpdateView):
    model = models.Student
    fields = '__all__'
    success_message = 'Student details updated successfully'

class DetailStudent(DetailView):
	context_object_name ='studentdetail'
	model = models.Student
	template_name = 'student/student_detail.html'