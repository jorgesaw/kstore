"""Core views."""

# Django
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class HomePageView(TemplateView):
    
    template_name = "core/home.html"

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Inicio"
        return context
    """
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "Inicio"})

class SamplePageView(TemplateView):

    template_name = "core/sample.html"