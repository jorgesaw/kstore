"""Slug base managers."""

# Django
from django.db import models

# Utilities
from django.utils.text import slugify

class SlugNameCreateManager(models.Manager):
    """Slug name create manager.
    
    Used to handle code creation.
    """

    def create(self, **kwargs):
        """Add a unique slug name from unique name."""

        name = kwargs['name']
        kwargs['slug_name'] = slugify(name)
        return super(SlugNameCreateManager, self).create(**kwargs)

