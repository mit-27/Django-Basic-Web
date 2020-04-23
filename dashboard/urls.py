from django.contrib import admin
from django.urls import path
from .views import dashboard_view, update_view, delete_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard/<int:id>/update', update_view, name='update-candidate'),
    path('dashboard/<int:id>/delete', delete_view, name='delete-candidate')
]
