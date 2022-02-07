from django.urls import path

from . import views

urlpatterns = [
    path('adminlist/', views.adminlist, name='adminlist'),
    path('createuser/', views.createuser, name='createuser'),
]
