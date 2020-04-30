"""Persons models."""

# Django
from django.db import models
from django.db import transaction

# Models
from apps.users.models import User

# Utilities
from apps.utils.models import BaseModel


class AbstractPerson(BaseModel, models.Model):
    """Abstract person model."""

    id_card = models.CharField(max_length=10, unique=True, verbose_name="DNI")
    fiscal_id_card = models.CharField(max_length=10, unique=True, verbose_name="CUIT")
    first_name = models.CharField(max_length=210, verbose_name="Nombre")
    last_name = models.CharField(max_length=210, verbose_name="Apellido")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento")
    desc = models.TextField(null=True, blank=True, verbose_name="Descripción")

    movile = models.CharField(max_length=50, null=True, blank=True, verbose_name="Celular")
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Teléfono")

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        abstract = True
        ordering = ['last_name', 'first_name']
        verbose_name = "persona"
        verbose_name_plural = "personas"

    def __str__(self):
        return self.full_name

class Person(AbstractPerson):
    """Person class."""

    pass


class PersonFiscal(Person):
    """Person fiscal class."""
    
    pass


class AbstractPersonWithUser(AbstractPerson):
    """Abstract person with user class."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = User(username='example@hostane.com')
        user.set_password(self.id_card)
        user.save()
        self.user = user
        super(AbstractPerson, self).save(*args, **kwargs)

class PersonWithUser(AbstractPersonWithUser):
    """Person with user class."""
    pass
