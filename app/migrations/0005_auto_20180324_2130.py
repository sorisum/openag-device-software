# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-24 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180324_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipetransition',
            options={'verbose_name': 'Recipe Transition', 'verbose_name_plural': 'Recipe Transitions'},
        ),
    ]
