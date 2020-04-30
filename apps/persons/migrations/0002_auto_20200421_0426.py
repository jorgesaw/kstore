# Generated by Django 2.2.10 on 2020-04-21 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonFiscal',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persons.Person')),
            ],
            options={
                'verbose_name': 'persona',
                'verbose_name_plural': 'personas',
                'ordering': ['last_name', 'first_name'],
                'abstract': False,
            },
            bases=('persons.person',),
        ),
        migrations.AlterField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person', verbose_name='persona'),
        ),
    ]
