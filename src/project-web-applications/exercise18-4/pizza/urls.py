"""Defines URL patterns for pizza"""

from django.urls import path

from . import views

app_name = 'pizza'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]