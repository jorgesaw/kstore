"""Registration URLs."""

from django.urls import path
from .views import registration as registration_views

urlpatterns = [
    path('signup/', registration_views.SignUpView.as_view(), name="signup"), 
    path('profile/', registration_views.ProfileUpdate.as_view(), name="profile"), 
    path('profile/email/', registration_views.EmailUpdate.as_view(), name="profile_email")
]
