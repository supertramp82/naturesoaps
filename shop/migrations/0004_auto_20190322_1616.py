# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-22 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190321_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='soap',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='soap',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
