# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20171127_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=0, verbose_name='Situação'),
        ),
    ]
