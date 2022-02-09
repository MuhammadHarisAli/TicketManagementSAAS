from django.urls import path

from . import views


urlpatterns = [
    path('property/', views.PropertyView.as_view(), name='property'),
    path('property/create/', views.propertyCreate, name='property_create'),
    path('property/update/<int:id>/', views.propertyupdate, name='property_update'),
    path('property/delete/(?P<id>\d+)/', views.propertyDelete, name='property_delete'),

    path('department/', views.department, name='department'),
    path('department/create/', views.departmentCreate, name='department_create'),
    path('department/update/<int:id>/', views.departmentupdate, name='department_update'),
    path('department/delete/(?P<id>\d+)/', views.departmentDelete, name='department_delete'),

    path('resource/', views.resource, name='resource'),
    path('resource/create/', views.resourceCreate, name='resource_create'),
    path('resource/update/<int:id>/', views.resourceupdate, name='resource_update'),
    path('resource/delete/(?P<id>\d+)/', views.resourceDelete, name='resource_delete'),
    path('sub_resource/delete/<int:sub_resource_id>/', views.subresourceDelete, name='sub_resource_delete'),
]
