"""Purchases forms."""

# Django
from django import forms
from django.utils import timezone

# Models
from apps.purchases.models import Purchase, Supplier
# Utilities
from apps.utils.forms import CustomDateInput


class PurchaseForm(forms.ModelForm):
    """Purchase form."""
    
    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        
        self.fields['subtotal'].disabled = True
        self.fields['total'].disabled = True
        
        supplier = forms.ModelChoiceField(
                    queryset=Supplier.objects.filter(active=True)
        )
        
    
    class Meta:
        """Meta class."""
        
        model = Purchase
        fields = ['number_purchase', 'date_purchase', 'observations', 
                    'is_fiscal', 'invoice_num', 'invoice_date', 
                    'discount', 'subtotal', 'total', 'supplier'  
                 ]
        widgets = {
            'number_purchase': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}), 
            'date_purchase': CustomDateInput(format=('%d-%m-%Y'), 
                                         attrs={'placeholder':'Selecciona una fecha', 
                                                'class': 'form-control'}), 
            'observations': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),  
            'invoice_num': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_date': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'subtotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        localized_fields = ('date_purchase', 'invoice_date')
