# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petdogs', '0005_auto_20171109_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatBreedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CatInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=50)),
                ('gender', models.BooleanField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('pet_breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petdogs.CatBreedInfo')),
            ],
        ),
        migrations.CreateModel(
            name='RabbitBreedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RabbitInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=50)),
                ('gender', models.BooleanField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('pet_breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petdogs.RabbitBreedInfo')),
            ],
        ),
    ]