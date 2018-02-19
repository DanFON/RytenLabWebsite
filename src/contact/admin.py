# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import contact

class contactAdmin(admin.ModelAdmin):
    class Meta:
        model = contact

admin.site.register(contact, contactAdmin)

def __str__(self):
    return '{}: {}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M:%S'), self.get_condition_display())