# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20180922_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleinfo',
            name='image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='article/%y/%m/%d', verbose_name='封面'),
        ),
    ]
