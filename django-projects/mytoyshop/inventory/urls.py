from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'inventory'

urlpatterns = [
	path('home', TemplateView.as_view(template_name='inventory/home.html'), \
		name='home'),
	path('add_category', views.AddCategory.as_view(),
		name='add_category'),
	path('update_category/<int:pk>/', views.UpdateCategory.as_view(),
		name='update_category'),
	path('categories', views.ListCategory.as_view(),
		name='categories'),
]