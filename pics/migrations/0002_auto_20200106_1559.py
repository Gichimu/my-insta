# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-06 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='photo',
        ),
    ]
