"""State models."""

# Django
from django.db import models

# Models
from apps.utils.models import BaseModelWithSlugName


class State(BaseModelWithSlugName):
    """State class."""

    name = models.CharField(max_length=210, verbose_name="Nombre")

    class Meta:
        """Meta class."""

        ordering = ['name']
        verbose_name = "provincia"
        verbose_name_plural = "provincias"


    def __str__(self):
        return '{}'.format(self.name)


