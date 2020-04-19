"""Products models."""

# Django
from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import pre_save

# Models
from .subcategories import SubCategory

# Utilities
from apps.utils.images import custom_upload_to
from apps.utils.models import BaseModelWithSlugName
from apps.utils.text import pre_save_receiver_slug_name


class AbstractProductWithoutPrice(BaseModelWithSlugName):
    """Abstract product with price.
    
    Model representing a product.
    """
    code = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name="Código interno")
    barcode = models.CharField(max_length=30, unique=True, verbose_name="Código de barras")
    name = models.CharField(max_length=210, verbose_name="Nombre")
    desc = models.CharField(max_length=255, verbose_name="Descripción")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    stock_min = models.PositiveIntegerField(default=0, verbose_name="Stock mínimo")
    stock_max = models.PositiveIntegerField(default=0, blank=True, verbose_name="Stock máximo")
    picture = models.ImageField(upload_to=custom_upload_to, blank=True, verbose_name="Imagen")

    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, verbose_name='Subcategoria')

    class Meta:
        """Meta class."""

        abstract = True
        ordering = ['name']
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return reverse_lazy('inventories:product', args=[str(self.slug_name),])

    def __str__(self):
        return '{}'.format(self.name)


class AbstractProduct(AbstractProductWithoutPrice):
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Precio")

    class Meta:
        """Meta class."""

        abstract = True


class Product(AbstractProduct):
    pass

pre_save.connect(pre_save_receiver_slug_name, sender=Product)


class ProductWithoutPrice(AbstractProductWithoutPrice):
    """Product without price."""

    class Meta:
        """Meta class."""

        verbose_name = "producto"
        verbose_name_plural = "productos"

pre_save.connect(pre_save_receiver_slug_name, sender=ProductWithoutPrice)

        
class ProductProxi(Product):
    """Product proxi."""

    class Meta:
        """Meta class."""

        proxy = True
        verbose_name_plural = "Stocks de productos"


class ProductWithoutPriceProxi(ProductWithoutPrice):
    """Product without price proxi."""

    class Meta:
        """Meta class."""

        proxy = True
        verbose_name_plural = "Stocks de productos sin precios"
