"""Categories forms."""

# Django
from django import forms

# Models
from apps.inventories.models import Category

class CategoryForm(forms.ModelForm):
    """Category form."""

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['active'].disabled = True

    class Meta:
        """Meta class."""
        
        model = Category
        fields = ['name', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'active': forms.CheckboxInput(attrs={'class': 'custom-control-input'})
        }

        
