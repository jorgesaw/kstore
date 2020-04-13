"""Profiles views."""

# Django
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Models
#from apps.registration.models import Profile
from apps.users.models import Profile


class ProfileListView(ListView):
    """Profile list view."""

    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 2

class ProfileDetailView(DetailView):
    """Profile detail view."""
    
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
