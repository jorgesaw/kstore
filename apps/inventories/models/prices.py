"""Prices model."""

# Django
from django.db import models
from django.urls import reverse_lazy

# Models
from .products import ProductWithoutPrice

# Utils
from apps.utils.models import BaseModel

        
class Price(models.Model):
    """Price model.
    
    Model representing a price.
    """

    value = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Valor")

    class Meta:
        """Meta class."""

        ordering = ['id']
        verbose_name = "precio"
        verbose_name_plural = "precios"

    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return ""#reverse_lazy('product-detail', args=[str(self.id)])

    def soft_delete(self):
        self.active = False
        self.save()

    def __str__(self):
        return '{}'.format(self.value)


class PriceWithDesc(Price):
    """Price with descount.
    
    Model representing a price.
    """
    desc = models.CharField(max_length=210, verbose_name="Tipo de precio")

    product = models.ForeignKey(ProductWithoutPrice, on_delete=models.CASCADE)

    class Meta:
        """Meta class."""
        
        ordering = ['desc']
        verbose_name = 'precio con descripcion'
        verbose_name_plural = 'precios con descripcion'

    def __str__(self):
        return '{} ({}) - $ {}'.format(self.product.name, self.desc, self.value)
