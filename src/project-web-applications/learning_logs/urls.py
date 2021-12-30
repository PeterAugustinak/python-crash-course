"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # single Topic view
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Add New Topic page
    path('new_topic/', views.new_topic, name = 'new_topic'),
    # Add New Entry page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Edit existing Entry page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
