# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maldini', '0024_tikacache'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='md5',
            field=models.CharField(db_index=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='sha1',
            field=models.CharField(db_index=True, max_length=50, null=True),
        ),
    ]