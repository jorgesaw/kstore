"""Items sales forms."""

# Django
from django import forms
from django.forms import BaseInlineFormSet
from django.forms.models import inlineformset_factory

# Models
from apps.sales.models import ( 
    ItemSale, 
    Sale
)


class BaseItemSaleInlineFormSet(BaseInlineFormSet):
    """Base item sale inline formset class."""
    
    def clean(self):
        super(BaseItemSaleInlineFormSet, self).clean()
        if any(self.errors):
            return
            
        for form in self.forms:
            if form.cleaned_data:
                price = form.cleaned_data['price']
                quantity = form.cleaned_data['quantity']
                
                if (price and quantity) is not None:
                     if not supplier_price > 0:
                        raise forms.ValidationError(
                            'Es obligatorio establecer un precio de venta al item', 
                            code='zero_negative_value'
                        )
                        
                     if not quantity > 0:
                        raise forms.ValidationError(
                            'Es obligatorio establecer una cantidad para el item', 
                            code='zero_negative_value'
                        )
        

class ItemSaleInlineForm(forms.ModelForm):
    """Item sale inline form."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['subtotal'].disabled = True
        self.fields['total'].disabled = True
        

    class Meta:
        """Meta class."""
        
        model = ItemSale
        exclude = ('created', 'modified')

    
ItemSaleInlineFormSet = inlineformset_factory(
    Sale, 
    ItemSale, 
    form=ItemSaleInlineForm,
    formset=BaseItemSaleInlineFormSet, 
    fields=['product', 'price', 'quantity', 'subtotal', 'discount', 'total'], 
    extra=1, 
    can_delete=True
)
