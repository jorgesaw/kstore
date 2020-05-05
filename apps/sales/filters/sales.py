"""Sales filters."""

# Django forms
from django import forms

# Django Filters
import django_filters
from django_filters import (
    CharFilter, 
    DateFilter, 
    BooleanFilter
)

# Models
from apps.sales.models import Sale


class SaleFilter(django_filters.FilterSet):
    """Sale filter."""

    number_sale = CharFilter( 
        field_name='number_sale', 
        lookup_expr='exact', 
        widget=forms.TextInput(
			attrs={'class': 'form-control', 
			'placeholder': 'Número interno'}),
    )
    
    receipt_num = CharFilter( 
        field_name='receipt_num', 
        lookup_expr='exact', 
        widget=forms.TextInput(
			attrs={'class': 'form-control', 
			'placeholder': 'Número remito'}),
    )        

    start_date = DateFilter(
        label='Fecha de compra desde', 
        field_name='date_sale', 
        lookup_expr='gte', 
        widget=forms.DateInput(
			attrs={'class': 'form-control', 
			'type': 'date'}),
    )

    end_date = DateFilter(
		label='Fecha de compra hasta', 
        field_name='date_sale', 
        lookup_expr='lte', 
        widget=forms.DateInput(
			attrs={'class': 'form-control', 
			'type': 'date'}),
    )
    customer = CharFilter(
        label='Cliente',  
        field_name='customer__last_name', 
        lookup_expr='icontains', 
        widget=forms.TextInput(
			attrs={'class': 'form-control', 
			'placeholder': 'Cliente'}),
    )
    
    class Meta:
        model = Sale
        fields = ('number_sale', 'receipt_num', 'start_date', 'end_date', 'customer', 'is_fiscal')
        localized_fields = ('date_sale',)

