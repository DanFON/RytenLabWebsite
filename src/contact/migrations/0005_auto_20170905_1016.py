# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20170904_1304'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='profiles',
        ),
    ]
