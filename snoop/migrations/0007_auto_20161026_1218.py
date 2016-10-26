# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-26 12:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

DEFAULT_COLLECTION_DESCRIPTION = "This collection was automatically " \
                                 "created by the snoop setup."

CREATE_DEFAULT_COLLECTION = """
INSERT INTO snoop_collection (id, slug, title, description)
VALUES (
  1,
  "doc",
  "Default Collection",
  "This collection was automatically created by the snoop setup."
"""

DELETE_DEFAULT_COLLECTION = """
DELETE FROM snoop_collection
WHERE id = 1
"""

def forward(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    Document = apps.get_model('snoop', 'Document')
    document_count = Document.objects.using(db_alias).count()

    if document_count > 0:
        Collection = apps.get_model('snoop', 'Collection')
        try:
            es_index = settings.SNOOP_ELASTICSEARCH_INDEX
        except AttributeError:
            print("WARNING: The SNOOP_ELASTICSEARCH_INDEX "
                  "is not set, will default to 'snoop-index'!")
            es_index = 'snoop-index'

        Collection.objects.using(db_alias).bulk_create([
            Collection(
                id=1,
                slug='doc',
                title='Default Collection',
                es_index=es_index,
                description=DEFAULT_COLLECTION_DESCRIPTION,
            )
        ])

def reverse(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    Document = apps.get_model('snoop', 'Document')
    document_count = Document.objects.using(db_alias).count()

    if document_count > 0:
        Collection = apps.get_model('snoop', 'Collection')
        Collection.objects.using(db_alias).filter(id=1).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('snoop', '0006_delete_foldermark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('slug', models.CharField(db_index=True, max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('es_index', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RunPython(forward, reverse),
        migrations.AddField(
            model_name='document',
            name='collection',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='document_set',
                to='snoop.Collection'
            ),
            preserve_default=False,
        ),
    ]
