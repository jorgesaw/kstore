"""Suppliers forms."""

# Django
from django import forms
from django.utils import timezone

# Models
from apps.purchases.models import Supplier

# Utilities
from apps.utils.forms import CustomDateInput
  

class SupplierForm(forms.ModelForm):
    """Supplier form."""

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if not (field == 'active' or field == 'birth_date'): 
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

        self.fields['active'].disabled = True

    class Meta:
        """Meta class."""
        model = Supplier
        fields = ['id_card', 'fiscal_id_card', 'last_name', 'first_name', 'birth_date', 'desc', 'movile', 'telephone', 'active']
        
        widgets = {
            'id_card': forms.TextInput(attrs={'autofocus': 'autofocus'}),
            'active': forms.CheckboxInput(attrs={'class': 'custom-control-input'}), 
            'birth_date': CustomDateInput(format=('%d-%m-%Y'), 
                                         attrs={'type':'date', 'placeholder':'Selecciona una fecha', 
                                                'class': 'form-control'})
        }

