"""Item sale models."""

# Python
from decimal import Decimal

# Django
from django.db import models
from django.db.models import Sum, F, FloatField, Max
from django.db.models.signals import post_save, pre_save
from django.db import transaction
from django.dispatch import receiver 
from django.utils import timezone

# Models
from apps.utils.models import BaseModelWithoutStatus
from apps.inventories.models import Product
from .sales import Sale

TAX_CHOICES = [
    ("0 %", 0.0), 
    ("21 %", 0.21), 
    ("10.5 %", 0.105), 
]


class ItemSale(BaseModelWithoutStatus):
    """Item sale class."""

    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, verbose_name='Precio')
    quantity = models.FloatField(default=1, verbose_name='Cantidad')
    discount = models.DecimalField(default=0.0, blank=True, max_digits=8, decimal_places=2, verbose_name="Descuento")
    
    subtotal = models.DecimalField(default=0.0, blank=True, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0.0, blank=True, max_digits=10, decimal_places=2)
    
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, verbose_name="Producto")
 
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Venta")

    class Meta:
        ordering = ['id',]
        verbose_name = 'item venta'
        verbose_name_plural = 'item ventas'
        

    def calculate_subtotal(self):
        self.subtotal = self.price * Decimal.from_float(self.quantity)

    def calculate_total(self):
        self.calculate_subtotal()
        self.total = self.subtotal - self.discount

    def save(self, *args, **kwargs):
        super(ItemSale, self).save(*args, **kwargs)
        self.calculate_total()

        super(ItemSale, self).save(update_fields=['total'])

    @transaction.atomic
    def delete(self, *args, **kwargs):
        sale = self.sale
        product = self.product
        quantity = self.quantity

        super(ItemSale, self).delete(*args, **kwargs)
        purchase.calculate_total()

        stock = product.stock
        stock -= quantity
        product.stock = stock
        product.save(update_fields=['stock',])

    def __str__(self):
        return str(self.total)


@receiver(post_save, sender=ItemSale)
def update_total_sales_at_item(sender, instance, **kwargs):
    instance.sale.calculate_total()


@receiver(pre_save, sender=ItemSale)
def update_stock_in_article(sender, instance, **kwargs):
    try:
        old_instance = ItemSale.objects.get(id=instance.id)
    except ItemSale.DoesNotExist:
        old_instance = None

    if not old_instance:
        return

    old_stock = old_instance.quantity

    if old_instance.product.stock:
        old_instance.product.stock += old_stock
        old_instance.product.save(update_fields=['stock',])

