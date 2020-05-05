"""Categories filters."""

# Django Filters
import django_filters
from django_filters import CharFilter

# Models
from apps.inventories.models import Category

from django import forms

class CategoryFilter(django_filters.FilterSet):
	"""Category filter class."""

	name = CharFilter(
		field_name='name', 
		lookup_expr='icontains', 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Nombre'}),
	)

	class Meta:
		model = Category
		fields = ('name',)
