# Generated by Django 2.2.10 on 2020-04-19 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0002_auto_20200419_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('id_card', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('fiscal_id_card', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('first_name', models.CharField(max_length=210, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=210, verbose_name='Apellido')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('movile', models.CharField(blank=True, max_length=50, null=True, verbose_name='Celular')),
                ('telephone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'persona',
                'verbose_name_plural': 'personas',
                'ordering': ['last_name', 'first_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonWithUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('id_card', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('fiscal_id_card', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('first_name', models.CharField(max_length=210, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=210, verbose_name='Apellido')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('movile', models.CharField(blank=True, max_length=50, null=True, verbose_name='Celular')),
                ('telephone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('street', models.CharField(max_length=50, verbose_name='Calle')),
                ('number_street', models.CharField(max_length=18, verbose_name='Número')),
                ('floor', models.CharField(blank=True, max_length=18, null=True, verbose_name='Piso')),
                ('departament', models.CharField(blank=True, max_length=18, null=True, verbose_name='Departamento')),
                ('type_address', models.CharField(choices=[('Residencia', 'Residencia')], default='Residencia', max_length=12, verbose_name='Tipo de residencia')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.City', verbose_name='Ciudad')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.PersonWithUser', verbose_name='persona')),
            ],
            options={
                'verbose_name': 'dirección',
                'verbose_name_plural': 'direcciones',
                'ordering': ['street', 'number_street'],
            },
        ),
    ]