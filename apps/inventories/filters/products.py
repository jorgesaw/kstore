"""Products filters."""

# Django forms
from django import forms

# Django Filters
import django_filters
from django_filters import CharFilter

# Models
from apps.inventories.models import Product

class ProductFilter(django_filters.FilterSet):
	"""Product filter class."""

	code = CharFilter(
		field_name='code', 
		lookup_expr='exact', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Código interno'}),
	)
	barcode = CharFilter(
		field_name='barcode', 
		lookup_expr='exact', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Código de barras'}),
	)
	name = CharFilter(
		field_name='name', 
		lookup_expr='icontains', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Nombre'}),
	)
	category = CharFilter(
		label='Categoría', 
		field_name='subcategory__category__name', 
		lookup_expr='icontains', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Categoria'}),
	)
	subcategory = CharFilter(
		label='Subcategoría', 
		field_name='subcategory__name', 
		lookup_expr='icontains', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Subcategoria'}),
	)
	

	class Meta:
		model = Product
		fields = ('code', 'barcode', 'name', 'category', 'subcategory')

