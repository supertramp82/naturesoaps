# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Soap(models.Model):
    name = models.CharField(max_length=300, blank=True, default='')
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    item_id = models.CharField(max_length=30, default='soap#')
    quantity = models.IntegerField(default=0)
    isActive = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)
    image1 = models.ImageField(upload_to='images/')
    image1_tn = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2_tn = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3_tn = models.ImageField(upload_to='images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/', blank=True, null=True)
    image4_tn = models.ImageField(upload_to='images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/', blank=True, null=True)
    image5_tn = models.ImageField(upload_to='images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='images/', blank=True, null=True)
    image6_tn = models.ImageField(upload_to='images/', blank=True, null=True)
    image7 = models.ImageField(upload_to='images/', blank=True, null=True)
    image7_tn = models.ImageField(upload_to='images/', blank=True, null=True)
    image8 = models.ImageField(upload_to='images/', blank=True, null=True)
    image8_tn = models.ImageField(upload_to='images/', blank=True, null=True)
    image9 = models.ImageField(upload_to='images/', blank=True, null=True)
    image9_tn = models.ImageField(upload_to='images/', blank=True, null=True)
