"""Categories forms."""

# Django
from django import forms

# Models
from apps.inventories.models import Category, SubCategory


class SubCategoryForm(forms.ModelForm):
    """Subcategory form."""

    def __init__(self, *args, **kwargs):
        super(SubCategoryForm, self).__init__(*args, **kwargs)
        self.fields['active'].disabled = True

    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(active=True)
    )

    class Meta:
        """Meta class."""
        
        model = SubCategory
        fields = ['name', 'category', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'active': forms.CheckboxInput(attrs={'class': 'custom-control-input'})
        }

        
