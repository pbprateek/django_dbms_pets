# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 11:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petdogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breedinfo',
            name='hair_length',
        ),
        migrations.RemoveField(
            model_name='breedinfo',
            name='life_span',
        ),
    ]
