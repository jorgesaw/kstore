"""Purchases admin."""

# Django
from django.contrib import admin

# Actions Mixin
from apps.utils.admin.actions import (
    ActionDownloadData, 
    ActionFiscalStatus
)

# Admin
from apps.persons.admin import AddressAdmin

# Models
from apps.purchases.models import (
    Supplier, 
    Purchase, 
    ItemPurchase
)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Purchase admin."""

    fields = ( ('id_card', 'fiscal_id_card', 'last_name'), ('first_name', 'birth_date'), ('movile', 'telephone'), )
    readonly_fields = ('created', 'modified')
    list_display = ('id_card', 'fiscal_id_card', 'full_name', 'movile')
    ordering = ('last_name', 'first_name', 'id_card')
    search_fields = ('id_card', 'fiscal_id_card', 'last_name', 'first_name')
    date_hierarchy = 'modified'
    list_filter = ('last_name',)
    inlines = [AddressAdmin,]
    

class ItemPurchaseAdmin(admin.TabularInline):
    """Item purchase admin."""

    model = ItemPurchase
    autocomplete_fields = ('product',)
    fields = ('product', 'price', 'quantity', 'subtotal', 'discount', 'total')
    readonly_fields = ('subtotal', 'total')
    list_display = ('product', 'price', 'quantity', 'subtotal', 'discount', 'total')
    ordering = ('id',)
    list_editable = ('price', 'quantity', 'discount')
    list_select_related = ('product',)
    extra = 1


@admin.register(Purchase)
class PurchaseAdmin(ActionFiscalStatus, admin.ModelAdmin):
    """Purchase admin."""

    autocomplete_fields = ('supplier',)
    fieldsets = (
        ('Datos compra', {
            'fields': ( ('number_purchase', 'date_purchase',  
                'invoice_num', 'invoice_date', 'is_fiscal'), ('supplier', 'subtotal', 'total') )
        }),
        ('Datos complementarios', {
            'classes': ('collapse',),
            'fields': ('discount', 'tax', 'observations'),
        }),
    )
    readonly_fields = ('created', 'modified', 'subtotal', 'total')
    list_display = ('number_purchase', 'date_purchase', 'supplier', 'is_fiscal', 'total')
    ordering = ('date_purchase',)
    search_fields = ('number_purchase', 'supplier__id_card', 'supplier__last_name')
    date_hierarchy = 'date_purchase' 
    list_filter = ('date_purchase', 'supplier__id_card', 'supplier__last_name')
    list_select_related = ('supplier',)
    actions = ['fiscal_emited', 'fiscal_not_emited']
    inlines = [ItemPurchaseAdmin,]
