# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 19:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maldini', '0020_document_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue', models.CharField(max_length=100)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('started', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='job',
            unique_together=set([('queue', 'data')]),
        ),
    ]
