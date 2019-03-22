# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Soap


def home(request):

    soaps = Soap.objects
    return render(request, 'shop/home.html', {'soaps': soaps})
