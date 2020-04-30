"""Customers model."""

# Models
from apps.persons.models import PersonFiscal


class Customer(PersonFiscal):
    """Customer class."""

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        

