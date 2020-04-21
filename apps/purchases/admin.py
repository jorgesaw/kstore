"""Purchases admin."""

# Django
from django.contrib import admin

# Actions Mixin
from apps.utils.admin.actions import ActionDownloadData

# Models
from apps.persons.models import Address
from apps.purchases.models import Supplier


class AddressAdmin(admin.TabularInline):
    model = Address
    autocomplete_fields = ('city',)
    fields = ('street', 'number_street', 'city', 'type_address')
    list_display = ('get_address', 'city')
    ordering = ('id',)
    list_editable = ('street', 'number_street', 'city', 'type_address')
    list_select_related = ('city',)
    extra = 1

    def get_address(self, obj):
        return obj.__str__()
    get_address.short_description = "Dirección"


@admin.register(Supplier)
class PurchaseAdmin(admin.ModelAdmin):
    """Purchase admin."""

    fields = ( ('id_card', 'fiscal_id_card', 'last_name'), ('first_name', 'birth_date'), ('movile', 'telephone'), )
    readonly_fields = ('created', 'updated')
    list_display = ('id_card', 'fiscal_id_card', 'full_name', 'movile')
    ordering = ('last_name', 'first_name', 'id_card')
    search_fields = ('id_card', 'fiscal_id_card', 'last_name', 'first_name')
    date_hierarchy = 'updated'
    list_filter = ('last_name',)
    inlines = [AddressAdmin,]
    
