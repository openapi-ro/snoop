# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maldini', '0018_remove_error_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='container',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maldini.Document'),
        ),
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together=set([('container', 'path')]),
        ),
    ]
