# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=250)),
                ('customer_phoneno', models.CharField(max_length=500)),
                ('customer_Adress', models.CharField(max_length=100)),
                ('customer_pin', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]