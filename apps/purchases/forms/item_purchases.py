"""Item purchases forms."""

# Django
from django import forms
from django.forms import BaseInlineFormSet
from django.forms.models import inlineformset_factory

# Models
from apps.purchases.models import ( 
    ItemPurchase, 
    Purchase
)


class BaseItemPurchaseInlineFormSet(BaseInlineFormSet):
    """Base item purchase inline formset class."""
    
    def clean(self):
        super(BaseItemPurchaseInlineFormSet, self).clean()
        if any(self.errors):
            return
            
        for form in self.forms:
            if form.cleaned_data:
                supplier_price = form.cleaned_data['supplier_price']
                quantity = form.cleaned_data['quantity']
                
                if (supplier_price and quantity) is not None:
                     if not supplier_price > 0:
                        raise forms.ValidationError(
                            'Es obligatorio establecer un precio de compra al item', 
                            code='zero_negative_value'
                        )
                        
                     if not quantity > 0:
                        raise forms.ValidationError(
                            'Es obligatorio establecer una cantidad para el item', 
                            code='zero_negative_value'
                        )
        

class ItemPurchaseInlineForm(forms.ModelForm):
    """Item purchase inline form."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['subtotal'].disabled = True
        self.fields['total'].disabled = True
        

    class Meta:
        """Meta class."""
        
        model = ItemPurchase
        exclude = ('created', 'modified')

    
ItemPurchaseInlineFormSet = inlineformset_factory(
    Purchase, 
    ItemPurchase, 
    form=ItemPurchaseInlineForm,
    formset=BaseItemPurchaseInlineFormSet, 
    fields=['product', 'supplier_price', 'quantity', 'subtotal', 'discount', 'total'], 
    extra=1, 
    can_delete=True
)
