# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-23 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_campaing', '0002_auto_20171220_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalito',
            name='descripcion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='campaing',
            name='tipo',
            field=models.CharField(choices=[('castracion', 'Castración')], max_length=10),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='dni',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]