"""Core  URLs."""

# Django
from django.urls import include, path

# Views


urlpatterns = [
    # API REST users 
    path('', include(('apps.users.api.urls', 'api-users'), namespace='api-users')),    
]
