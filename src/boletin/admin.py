# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Registrado

class AdminResgistrado(admin.ModelAdmin):
    list_display = ["__unicode__", "nombre", "timestamp"]
    class Meta:
        model = Registrado

admin.site.register(Registrado, AdminResgistrado)
