"""Django models utilities."""

# Django
from django.db import models
from django.db.models.signals import pre_save 

# Models
from apps.utils.models_mixin import ModelWithSlugNameMixin


class BaseModel(models.Model):
    """Base model.

    BaseModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
        + active (Boolean): Store the active object.
    """

    created = models.DateTimeField(
        'created at', 
        auto_now_add=True, 
        #verbose_name="Fecha de creación",
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at', 
        auto_now=True, 
        help_text='Date time on which the object was last modified.'
    )
        
    active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']

    def soft_delete(self):
        self.active = False
        self.save()

    def delete(self, *args, **kwargs):
        self.soft_delete()

    def get_dict_fields_and_values(self):
        return dict((field.name, field.value_to_string(self))
                                            for field in self._meta.fields)


class BaseModelWithSlugName(BaseModel):
    """Base model with slug name.

    BaseModel acts as an abstract base class from which every
    model new in the project will inherit. This class provides
    every table with the following attributes:
        + slug_name (String): Store the slug name.
    """
    
    slug_name = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta(BaseModel.Meta):
        """Meta option."""

        abstract = True

