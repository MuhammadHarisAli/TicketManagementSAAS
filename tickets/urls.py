from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tickets/', views.tickets, name='tickets'),
    path('tickets/create/', views.ticketsCreate, name='tickets_create'),
    path('tickets/update/<int:id>/', views.ticketsUpdate, name='tickets_update'),
    path('tickets/delete/(?P<id>\d+)/', views.ticketsDelete, name='tickets_delete'),
]
