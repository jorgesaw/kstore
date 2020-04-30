"""Sales admin."""

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
from apps.sales.models import (
    Customer, 
    Sale, 
    ItemSale
)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer admin."""

    fields = ( ('id_card', 'fiscal_id_card', 'last_name'), ('first_name', 'birth_date'), ('movile', 'telephone'), )
    readonly_fields = ('created', 'modified')
    list_display = ('id_card', 'fiscal_id_card', 'full_name', 'movile')
    ordering = ('last_name', 'first_name', 'id_card')
    search_fields = ('id_card', 'fiscal_id_card', 'last_name', 'first_name')
    date_hierarchy = 'modified'
    list_filter = ('last_name',)
    inlines = [AddressAdmin,]
    
    
class ItemSaleAdmin(admin.TabularInline):
    """Item sale admin."""

    model = ItemSale
    autocomplete_fields = ('product',)
    fields = ('product', 'price', 'quantity', 'subtotal', 'discount', 'total')
    readonly_fields = ('subtotal', 'total')
    list_display = ('product', 'price', 'quantity', 'subtotal', 'discount', 'total')
    ordering = ('id',)
    list_editable = ('product__price', 'quantity', 'discount')
    list_select_related = ('product',)
    extra = 1


@admin.register(Sale)
class SaleAdmin(ActionFiscalStatus, admin.ModelAdmin):
    """Sale admin."""

    autocomplete_fields = ('customer',)
    fieldsets = (
        ('Datos venta', {
            'fields': ( ('number_sale', 'date_sale',  
                'receipt_num', 'receipt_date', 'is_fiscal'), ('customer', 'subtotal', 'total') )
        }),
        ('Datos complementarios', {
            'classes': ('collapse',),
            'fields': ('discount', 'tax', 'observations'),
        }),
    )
    
    readonly_fields = ('created', 'modified', 'subtotal', 'total')
    list_display = ('number_sale', 'date_sale', 'customer', 'is_fiscal', 'total')
    ordering = ('date_sale',)
    search_fields = ('number_sale', 'customer__id_card', 'customer__last_name')
    date_hierarchy = 'date_sale' 
    list_filter = ('date_sale', 'customer__id_card', 'customer__last_name')
    list_select_related = ('customer',)
    actions = ['fiscal_emited', 'fiscal_not_emited']
    inlines = [ItemSaleAdmin,]

