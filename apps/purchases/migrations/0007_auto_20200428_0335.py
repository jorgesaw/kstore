# Generated by Django 2.2.10 on 2020-04-28 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0006_purchase_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='invoic_date',
            new_name='invoice_date',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchases.Supplier', verbose_name='Proveedor'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Impuesto'),
        ),
    ]
