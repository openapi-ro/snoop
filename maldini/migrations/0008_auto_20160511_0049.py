# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maldini', '0007_auto_20160511_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cache',
            name='document',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='maldini.Document'),
        ),
    ]