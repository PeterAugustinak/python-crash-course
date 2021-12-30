"""Defines URL patterns for pizza"""

from django.urls import path

from . import views

app_name = 'pizza'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pizzas page
    path('pizzas/', views.pizzas, name='pizzas'),
    # detail page for a single Pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]