from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('create/', views.create, name='create'),
	path('edit/<code>', views.edit, name='edit'),
	path('delete/<code>', views.delete, name='delete'),
]

