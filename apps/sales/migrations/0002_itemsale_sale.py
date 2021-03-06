# Generated by Django 2.2.10 on 2020-04-30 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('number_sale', models.CharField(blank=True, max_length=18, null=True, verbose_name='Número interno')),
                ('date_sale', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('receipt_num', models.CharField(blank=True, max_length=30, null=True, verbose_name='N° de factura')),
                ('is_fiscal', models.BooleanField(default=True, verbose_name='Es fiscal')),
                ('receipt_date', models.DateField(verbose_name='Fecha de la factura de compra')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Descuento')),
                ('tax_choices', models.CharField(blank=True, choices=[('0 %', 0.0), ('21 %', 0.21), ('10.5 %', 0.105)], default='0 %', max_length=2, null=True, verbose_name='IVA')),
                ('tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Impuesto')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.Customer', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'venta',
                'verbose_name_plural': 'ventas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ItemSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio')),
                ('quantity', models.FloatField(default=1, verbose_name='Cantidad')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, verbose_name='Descuento')),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventories.Product', verbose_name='Producto')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Sale', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'item venta',
                'verbose_name_plural': 'item ventas',
                'ordering': ['id'],
            },
        ),
    ]
