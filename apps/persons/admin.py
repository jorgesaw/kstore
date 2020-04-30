"""Address admin."""

# Django
from django.contrib import admin

# Models
from apps.persons.models import Address


class AddressAdmin(admin.TabularInline):
    """Address admin."""

    model = Address
    autocomplete_fields = ('city',)
    fields = ('street', 'number_street', 'city', 'type_address')
    list_display = ('get_address', 'city')
    ordering = ('id',)
    list_editable = ('street', 'number_street', 'city', 'type_address')
    list_select_related = ('city', 'person')
    extra = 1

    def get_address(self, obj):
        return obj.__str__()
    get_address.short_description = "Dirección"
