# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170517_0412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=500)),
                ('adress', models.CharField(max_length=100)),
                ('email_ID', models.CharField(max_length=1000)),
                ('Pincode', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
