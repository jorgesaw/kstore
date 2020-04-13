"""Profiles URLs."""

# Django
from django.urls import path

# Views
from .views import (
    ProfileListView, 
    ProfileDetailView
    )

urlpatterns = [
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
]
