# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-03 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurents', '0002_auto_20190303_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='updated',
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
