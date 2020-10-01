
from django.urls import path, include

from . import views

app_name = 'student'

urlpatterns = [
	path('redirect_student/<int:pk>', views.RedirectStudent.as_view(), \
		name='redirect_student'),
    path('add_student', views.AddStudent.as_view(), \
    	name='add_student'),
    path('update_student/<int:pk>', views.UpdateStudent.as_view(), \
    	name='update_student'),
    path('detail_student/<int:pk>', views.DetailStudent.as_view(), \
    	name='detail_student')
]