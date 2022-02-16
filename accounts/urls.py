from django.urls import path

from . import views

urlpatterns = [
    path('adminlist/', views.adminlist, name='adminlist'),
    path('createuser/', views.createuser, name='createuser'),
    path('staff/', views.staff_list, name='staff_list'),
    path('create_staff/', views.create_staff, name='create_staff'),

]
