"""Purchases filters."""

# Django Filters
import django_filters
from django_filters import (
    CharFilter, 
    DateFilter, 
    BooleanFilter
)

# Models
from apps.purchases.models import Purchase
from django import forms

class PurchaseFilter(django_filters.FilterSet):
    """Purchase filter."""

    number_purchase = CharFilter( 
        field_name='number_purchase', 
        lookup_expr='exact', 
        widget=forms.TextInput(
			attrs={'class': 'form-control', 
			'placeholder': 'Número interno'}),
    )
    
    invoice_num = CharFilter( 
        field_name='invoice_num', 
        lookup_expr='exact', 
        widget=forms.TextInput(
			attrs={'class': 'form-control', 
			'placeholder': 'Número factura'}),
    )        

    start_date = DateFilter(
        label='Fecha de compra desde', 
        field_name='date_purchase', 
        lookup_expr='gte', 
        widget=forms.DateInput(
			attrs={'class': 'form-control', 
			'type': 'date'}),
    )

    end_date = DateFilter(
		label='Fecha de compra hasta', 
        field_name='date_purchase', 
        lookup_expr='lte', 
        widget=forms.DateInput(
			attrs={'class': 'form-control', 
			'type': 'date'}),
    )
    supplier = CharFilter(
        label='Proveedor',  
        field_name='supplier__last_name', 
        lookup_expr='icontains', 
        widget=forms.TextInput(
			attrs={'class': 'form-control', 
			'placeholder': 'Proveedor'}),
    )
    
    class Meta:
        model = Purchase
        fields = ('number_purchase', 'invoice_num', 'start_date', 'end_date', 'is_fiscal')
        localized_fields = ('date_purchase',)

