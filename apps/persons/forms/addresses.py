"""Addresses forms."""

# Django
from django import forms

# Extra views
from extra_views import InlineFormSetFactory

# Models
from apps.persons.models import Address
from apps.locations.models import City


class AddressInlineForm(InlineFormSetFactory):
    """Address inline form."""

    model = Address
    fields = ['street', 'number_street', 'city']
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': False, 
                      'widgets' : {
                        'street': forms.TextInput(attrs={'class': 'form-control'}), 
                        'number_street': forms.TextInput(attrs={'class': 'form-control'}), 
                      }    
    }
    city= forms.ModelChoiceField(queryset=City.objects.filter(active=True))


class AddressInlineUpdateForm(AddressInlineForm):
    """Address inline update form."""

    factory_kwargs = {'extra': 0, 'max_num': None,
                      'can_order': False, 'can_delete': False, 
                      'widgets' : {
                        'street': forms.TextInput(attrs={'class': 'form-control'}), 
                        'number_street': forms.TextInput(attrs={'class': 'form-control'}), 
                      }    
    }
