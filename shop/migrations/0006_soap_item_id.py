# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-22 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_soap_createddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='soap',
            name='item_id',
            field=models.CharField(default='soap#', max_length=30),
        ),
    ]
