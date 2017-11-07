# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Registrado

class AdminResgistrado(admin.ModelAdmin):
    list_display = ["email", "nombre", "timestamp"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]
    class Meta:
        model = Registrado

admin.site.register(Registrado, AdminResgistrado)
