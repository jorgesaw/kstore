"""Custom text functions."""

# Utilities
from django.utils.text import slugify

def pre_save_receiver_slug_name(sender, instance, *args, **kwargs):
    """Pre save receiver."""

    instance.slug_name = slugify(instance.name)


