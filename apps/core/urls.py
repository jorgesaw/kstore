"""Core  URLs."""

# Django
from django.urls import include, path

# Views
from .views import core as core_views

urlpatterns = [
    path('', core_views.HomePageView.as_view(), name="home"),
]
