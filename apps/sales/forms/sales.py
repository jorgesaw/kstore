"""Sales forms."""

# Django
from django import forms
from django.utils import timezone

# Models
from apps.sales.models import Sale, Customer
# Utilities
from apps.utils.forms import CustomDateInput


class SaleForm(forms.ModelForm):
    """Purchase form."""
    
    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        
        self.fields['subtotal'].disabled = True
        self.fields['total'].disabled = True
        
        customer = forms.ModelChoiceField(
                    queryset=Customer.objects.filter(active=True)
        )
        
    
    class Meta:
        """Meta class."""
        
        model = Sale
        fields = ['number_sale', 'date_sale', 'observations', 
                    'is_fiscal', 'receipt_num', 'receipt_date', 
                    'discount', 'subtotal', 'total', 'customer'  
                 ]
        widgets = {
            'number_sale': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}), 
            'date_sale': CustomDateInput(format=('%d-%m-%Y'), 
                                         attrs={'placeholder':'Selecciona una fecha', 
                                                'class': 'form-control'}), 
            'observations': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),  
            'receipt_num': forms.TextInput(attrs={'class': 'form-control'}),
            'receipt_date': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'subtotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        localized_fields = ('date_sale', 'receipt_date')
        
