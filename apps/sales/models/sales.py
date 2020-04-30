"""Sales model."""

# Python
from decimal import Decimal

# Django
from django.db import models
from django.db.models import Sum, F, FloatField, Max 
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse_lazy

# Models
from apps.utils.models import BaseModel
from apps.sales.models import Customer
from apps.users.models import User

TAX_CHOICES = [
    ("0 %", 0.0), 
    ("21 %", 0.21), 
    ("10.5 %", 0.105), 
]


class Sale(BaseModel):
    """Sale class."""

    # Internal number to send
    number_sale = models.CharField(
        max_length=18, 
        blank=True, 
        null=True,
        verbose_name='Número interno'
    ) 
    
    date_sale = models.DateField(default=timezone.now, verbose_name='Fecha')
    observations = models.TextField(blank=True, null=True, verbose_name='Observaciones')
    
    # Invoice data
    receipt_num = models.CharField(
                    max_length=30, 
                    blank=True, 
                    null=True, 
                    verbose_name='N° de factura'
    )
    
    is_fiscal = models.BooleanField(default=True, verbose_name="Es fiscal")    
    receipt_date = models.DateField(verbose_name='Fecha de la factura de compra')
    
    # Values
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Descuento')
    tax_choices = models.CharField(
                    blank=True, 
                    null=True, 
                    max_length=2, 
                    choices=TAX_CHOICES, 
                    default="0 %", 
                    verbose_name="IVA"
    )
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Impuesto')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Cliente')
    created_by = models.ForeignKey(User, related_name="customers", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-id',]
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'
        
    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        
        return reverse_lazy('sales:sale-update', kwargs={'pk': self.pk})
        

    def _calculate_subtotal(self):
        
        # Devuelve un diccionario con un dato cuya key es 'subtotal_purchase'
        _subtotal = self.itemsale_set.all().aggregate(
            subtotal_sale=Sum( ( F('quantity') * F('price') ) - F('discount'), output_field=FloatField() )  
        )['subtotal_sale'] or 0
        
        self.subtotal = _subtotal

    def calculate_total(self):
        
        self._calculate_subtotal()
        
        _total = float(self.subtotal) - float(self.discount) + float(self.tax) 
        self.total = Decimal.from_float(_total)
        
        Sale.objects.filter(id=self.id).update(subtotal=self.subtotal, total=_total)
    
    def __str__(self):
        return self.number_sale  
    

@receiver(post_save, sender=Sale)
def update_sales_total(sender, instance, **kwargs):
    instance.calculate_total()

