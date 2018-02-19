# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length = 120)
    description = models.CharField(max_length=120)
    location = models.CharField(max_length = 120,default='my location default', blank=True, null=True)
    Research = models.CharField(max_length = 120,null=True)
    image = models.ImageField(upload_to ='profile_image', blank=True)

    def _unicode_(self):
       return self.name