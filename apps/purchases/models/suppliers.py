"""Supliers model."""

# Models
from apps.persons.models import PersonFiscal


class Supplier(PersonFiscal):
    """Supplier class."""

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        
