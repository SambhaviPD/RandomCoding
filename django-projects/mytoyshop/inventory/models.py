from django.urls import reverse
from django.db import models
from django.conf import settings
 
# Create your models here.
 
# Table to hold Category details
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name= \
       'Category name')
    description = models.TextField(verbose_name = \
       'Detailed description')
 
    class Meta:
       unique_together = ['name',]

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('inventory:update_category', kwargs={'pk':self.pk})

# Table to hold details about each Toy
class Toy(models.Model):
    name = models.CharField(max_length=100, verbose_name= \
       'Toy name')
    category = models.ForeignKey(Category, \
       on_delete=models.CASCADE, \
       verbose_name='Category of Toy')
    description = models.TextField(verbose_name = \
       'Detailed description')
    cost = models.DecimalField(max_digits=6, decimal_places=2, \
       verbose_name='Cost of Toy in INR')
    brand = models.CharField(max_length=100, verbose_name= \
       'Brand of Toy')
    ACTIVITY_TYPE_CHOICES = (
       ('Indoor', 'Indoor'),
       ('Outdoor', 'Outdoor'),
    )
    activity_type = models.CharField(max_length=20, choices=\
       ACTIVITY_TYPE_CHOICES, verbose_name='Activity type')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  \
      on_delete=models.CASCADE)
     
    class Meta:
        unique_together = ['name', 'category']
     
    def __str__(self):
        return '{0} - {1}'.format(self.name, self.category)

    def get_absolute_url(self):
      return reverse('inventory:update_toy', kwargs={'pk':self.pk})