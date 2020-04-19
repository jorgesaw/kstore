"""Locations admin."""

# Django
from django.contrib import admin

# Models
from apps.locations.models import (
    City, 
    State
)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """City admin."""

    autocomplete_fields = ('state',)
    fields = ( 'name', 'zip_city', 'ddn', 'state')
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'zip_city', 'ddn', 'state')
    ordering = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'modified' # Jerarquizar por fechas
    list_filter = ('name',)
    list_editable = ('zip_city', 'ddn')
    list_select_related = ('state',)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """State admin."""

    fields = ( 'name',)
    readonly_fields = ('created', 'modified')
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'modified' # Jerarquizar por fechas
    list_filter = ('name',)
   
