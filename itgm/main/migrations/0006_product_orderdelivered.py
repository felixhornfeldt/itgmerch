# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orderDelivered',
            field=models.BooleanField(default=False),
        ),
    ]
