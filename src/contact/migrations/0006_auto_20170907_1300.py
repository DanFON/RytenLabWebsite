# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20170905_1016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profiles',
            new_name='contact',
        ),
    ]
