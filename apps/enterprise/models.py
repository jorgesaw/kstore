"""Enterprise models."""

# Django
from django.db import models
from django.db.models.signals import pre_save

# Models
from apps.utils.models import BaseModelWithSlugName

# Utilities
from apps.utils.images import custom_upload_to
from apps.utils.text import pre_save_receiver_slug_name


class Enterprise(BaseModelWithSlugName):
    """Enterprise class.
    
    Model representing at enterprise data.
    """
    fiscal_code = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name="CUIT")
    name = models.CharField(max_length=210, verbose_name="Nombre")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Inicio de actividades")
    desc = models.TextField(null=True, blank=True, verbose_name="Descripción")
    movile = models.CharField(max_length=50, null=True, blank=True, verbose_name="Celular")
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Teléfono")
    picture = models.ImageField(upload_to=custom_upload_to, blank=True, verbose_name="Imagen")

    class Meta:
        """Meta class."""

        ordering = ['name']
        verbose_name = "empresa"
        verbose_name_plural = "empresa"


    def __str__(self):
        return '{}'.format(self.name)

pre_save.connect(pre_save_receiver_slug_name, sender=Enterprise)
