from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    semester = models.CharField(max_length=10)
    favorite1 = models.CharField(max_length=100, \
        verbose_name='Favorite Subject1')
    favorite2 = models.CharField(max_length=100, \
        verbose_name='Favorite Subject2')
    favorite3 = models.CharField(max_length=100, \
        verbose_name='Favorite Subject3')

    def __str__(self):
    	return "{0} {1}".format(self.name, 
    		self.semester)

    def get_absolute_url(self):
    	return reverse('student:detail_student', \
    		kwargs={'pk':self.pk})