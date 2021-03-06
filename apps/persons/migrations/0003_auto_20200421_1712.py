# Generated by Django 2.2.10 on 2020-04-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20200421_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='fiscal_id_card',
            field=models.CharField(max_length=10, unique=True, verbose_name='CUIT'),
        ),
        migrations.AlterField(
            model_name='personwithuser',
            name='fiscal_id_card',
            field=models.CharField(max_length=10, unique=True, verbose_name='CUIT'),
        ),
    ]
