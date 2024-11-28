from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add_musician, name='add_musician'),
    path('edit/<int:id>/', views.edit_musician, name='edit_musician'),
]