# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20170717_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='title',
            new_name='stock',
        ),
    ]
