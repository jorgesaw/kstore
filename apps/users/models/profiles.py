"""Profile model."""

# Django
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Utilities
from apps.utils.models import BaseModel
from apps.utils.images import custom_upload_to 

# Models
from .users import User


class Profile(BaseModel):
    """Profile model.

    A profile holds a user's public data like biography, picture 
    and statics
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture', 
        upload_to=custom_upload_to,
        null=True,
        blank=True 
    )

    biography = models.TextField(max_length=500, null=True, blank=True)

    website = models.URLField(
        max_length=255, 
        null=True, 
        blank=True, 
        verbose_name="Website"
    )

    class Meta:
        """Meta class."""

        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
        ordering = ['user__username', ]

    def __str__(self):
        """Return user's str representation"""
        return str(self.user)


#@receiver(post_save, sender=User)
#def ensure_profile_exists(sender, instance, **kwargs):
    """
    Señal que se encarga de crear un perfil por defecto en caso de que 
    el usuario se cree una cuenta (post_save) pero nunca ingrese a su perfil.
    """
 #   if kwargs.get('created', False): # Si acaba de crearse un usuario creamos el perfil
  #      Profile.objects.get_or_create(user=instance)
        
