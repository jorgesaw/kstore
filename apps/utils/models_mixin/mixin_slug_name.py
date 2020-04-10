"""Model with slug name mixin."""

# Utilities
from django.utils.text import slugify


class ModelWithSlugNameMixin:
    """Model with slug name mixin.

    Add custom slugify name by defect.
    """

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(ModelWithSlugNameMixin, self).save(*args, **kwargs)