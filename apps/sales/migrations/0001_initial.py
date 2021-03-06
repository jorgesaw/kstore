# Generated by Django 2.2.10 on 2020-04-30 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0003_auto_20200421_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('personfiscal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persons.PersonFiscal')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
            bases=('persons.personfiscal',),
        ),
    ]
