# Generated by Django 2.2.10 on 2020-04-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0007_auto_20200428_0335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-id'], 'verbose_name': 'compra', 'verbose_name_plural': 'compras'},
        ),
        migrations.AlterField(
            model_name='itempurchase',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='itempurchase',
            name='quantity',
            field=models.FloatField(default=1, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='itempurchase',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='itempurchase',
            name='supplier_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='itempurchase',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
