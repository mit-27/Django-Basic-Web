from django.contrib import admin
from django.urls import path
from .views import candidate_view

urlpatterns = [
    path('add/', candidate_view, name='add-candidate'),
]
