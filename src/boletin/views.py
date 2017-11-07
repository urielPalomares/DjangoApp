# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import RegForm

from django.shortcuts import render

# Create your views here.

def inicio(request):
    form = RegForm()
    context = {
        "el_form": form,
    }
    return render(request, "inicio.html", context)
