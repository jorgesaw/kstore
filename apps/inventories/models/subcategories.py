"""Subcategories models."""

# Django
from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import pre_save

# Models
from .categories import Category

# Utils
from apps.utils.models import BaseModelWithSlugName
from apps.utils.text import pre_save_receiver_slug_name

class SubCategory(BaseModelWithSlugName):
    """Subcategory.
    
    Model representing a subcategory of product.
    """

    name = models.CharField(max_length=150, verbose_name="Nombre")
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        verbose_name='Categoria'
    )

    class Meta:
        """Meta class."""

        ordering = ['-created']
        verbose_name = "subcategoria"
        verbose_name_plural = "subcategorias"
        unique_together = ('category', 'name')

    def get_absolute_url(self):
        """Returns the url to access a particular subcategory instance."""
        return reverse_lazy('inventories:subcategory', args=[str(self.slug_name),])

    def __str__(self):
        return '{} ({})'.format(self.name, self.category.name)

pre_save.connect(pre_save_receiver_slug_name, sender=SubCategory)

