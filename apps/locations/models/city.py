"""City models."""

# Django
from django.db import models

# Models
from apps.utils.models import BaseModelWithSlugName
from .state import State


class City(BaseModelWithSlugName):
    """City class."""

    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    zip_city = models.CharField(max_length=30, null=True, blank=True, verbose_name="Código postal")
    ddn = models.CharField(max_length=12, null=True, blank=True, verbose_name="Característica")

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name='Provincia')


    class Meta:
        """Meta class."""

        ordering = ['name']
        verbose_name = "ciudad"
        verbose_name_plural = "ciudades"


    def __str__(self):
        return '{}'.format(self.name)


