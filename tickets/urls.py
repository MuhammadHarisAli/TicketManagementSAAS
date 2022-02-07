from django.urls import path

from tickets.views import index

urlpatterns = [
    path('', index, name='index'),
]
