# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170517_1449'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Detail',
            new_name='Customer',
        ),
    ]
