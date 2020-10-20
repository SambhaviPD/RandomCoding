from django.urls import path, include

from . import views

app_name = 'inventory'

urlpatterns = [
	path('add_category', views.AddCategory.as_view(),
		name='add_category'),
	path('update_category/<int:pk>/', views.UpdateCategory.as_view(),
		name='update_category'),
	path('categories', views.ListCategory.as_view(),
		name='categories'),
]
