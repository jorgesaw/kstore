"""Suppliers filters."""

# Django forms
from django import forms

# Django Filters
import django_filters
from django_filters import CharFilter

# Models
from apps.purchases.models import Supplier


class SupplierFilter(django_filters.FilterSet):
	"""Supplier filter class."""

	last_name = CharFilter(
		field_name='last_name', 
		lookup_expr='icontains', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Apellido'}),
	)
	id_card = CharFilter(
		field_name='id_card', 
		lookup_expr='exact', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'DNI'}),
	)
	fiscal_id_card = CharFilter(
		field_name='fiscal_id_card', 
		lookup_expr='exact', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'CUIT'}),
	)
	address = CharFilter(
		label='Ciudad', 
		field_name='address__city__name', 
		lookup_expr='icontains', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Ciudad'}),
	)

	class Meta:
		model = Supplier
		fields = ('id_card', 'fiscal_id_card', 'last_name', 'address')

