# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docassist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='material_name',
        ),
        migrations.AddField(
            model_name='material',
            name='disease',
            field=models.CharField(default='', max_length=300),
        ),
    ]