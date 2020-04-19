"""Categories models."""

# Django
from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import pre_save

# Utils
from apps.utils.models import BaseModelWithSlugName
from apps.utils.text import pre_save_receiver_slug_name


class AbstractCategory(BaseModelWithSlugName):
    """Abstract category.
    
    Model representing a category of product.
    """

    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    class Meta:
        """Meta class."""

        abstract = True
        ordering = ['-created']
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def get_absolute_url(self):
        """Returns the url to access a particular category instance."""
        return reverse_lazy('inventories:category', args=[str(self.slug_name),])

    def __str__(self):
        return self.name

class Category(AbstractCategory):
    """Category class."""
    
    pass

pre_save.connect(pre_save_receiver_slug_name, sender=Category)

