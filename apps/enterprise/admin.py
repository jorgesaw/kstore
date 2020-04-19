"""Enterprise admin."""

# Django
from django.contrib import admin

# Models
from apps.enterprise.models import Enterprise

# Mixin
from apps.utils.admin import ActiveModelSuperUserMixin


@admin.register(Enterprise)
class CategoryAdmin(ActiveModelSuperUserMixin, admin.ModelAdmin):
    """Enterprise admin."""

    fields = ('name', 'fiscal_code', 'desc', 'telephone', 'movile')
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'fiscal_code', 'desc')
   
