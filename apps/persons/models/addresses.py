"""Adrresses models."""

# Django
from django.db import models

# Models
from .persons import PersonWithUser
from apps.locations.models import City
from apps.utils.models import BaseModel


DEFAULT_TYPE_ADDRESS = "Residencia"
TYPE_ADDRESS_CHOICES = (
    (DEFAULT_TYPE_ADDRESS, DEFAULT_TYPE_ADDRESS), 
)

class Address(BaseModel, models.Model):
    """Address model."""
    
    street = models.CharField(max_length=50, verbose_name='Calle')
    number_street = models.CharField(max_length=18, verbose_name='Número')
    floor = models.CharField(max_length=18, null=True, blank=True, verbose_name='Piso')
    departament = models.CharField(max_length=18, null=True, blank=True, verbose_name='Departamento')

    type_address = models.CharField(max_length=12, choices=TYPE_ADDRESS_CHOICES, default=DEFAULT_TYPE_ADDRESS, verbose_name='Tipo de residencia')

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Ciudad')
    person = models.ForeignKey(PersonWithUser, on_delete=models.CASCADE,  verbose_name='persona')

    class Meta:
        ordering = ['street', 'number_street']
        verbose_name = "dirección"
        verbose_name_plural = "direcciones"


    def __str__(self):
        return '{} {}'.format(self.street, self.number_street)

