# Generated by Django 5.0.2 on 2024-06-03 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('stock', models.IntegerField(default=0, null=True)),
                ('genero', models.CharField(choices=[('1', 'Acción'), ('2', 'Aventura'), ('3', 'Carrera')], max_length=1, verbose_name='Género')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='articulos.categoria', verbose_name='Categoría')),
            ],
        ),
    ]
