"""Products forms."""

# Django
from django import forms

# Models
from apps.inventories.models import (
    Product, 
    ProductWithoutPrice, 
    SubCategory
)


class ProductForm(forms.ModelForm):
    """Product form."""

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['active'].disabled = True

    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.filter(active=True)
    )
    
    class Meta:
        """Meta class."""
        model = Product
        fields = ['name', 'code', 'barcode', 'desc', 'picture', 'price', 'stock', 'stock_min', 'stock_max', 'subcategory', 'active']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'barcode': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'custom-control-input'})
        }

class ProductWithoutPriceForm(forms.ModelForm):
    """Product without price form."""

    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.filter(active=True)
    )

    class Meta:
        """Meta class."""
        
        model = ProductWithoutPrice
        fields = ['name', 'code', 'desc', 'picture', 'stock', 'stock_min', 'stock_max', 'subcategory', 'active']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'code': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'custom-control-input'})
        }

