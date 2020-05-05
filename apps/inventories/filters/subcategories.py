"""SubCategories filters."""

# Django forms
from django import forms

# Django Filters
import django_filters
from django_filters import CharFilter

# Models
from apps.inventories.models import Category, SubCategory

class SubCategoryFilter(django_filters.FilterSet):
	"""SubCategory filter class."""

	name = CharFilter(
		field_name='name', 
		lookup_expr='icontains', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Nombre'}),
	)

	category = CharFilter(
		label='Categoría', 
		field_name='category__name', 
		lookup_expr='icontains', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Categoria'}),
	)

	class Meta:
		model = SubCategory
		fields = ('name', 'category')
