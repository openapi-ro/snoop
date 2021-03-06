# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-27 14:54
from __future__ import unicode_literals

from django.db import migrations


def refactor_exceptions(apps, schema_editor):
    broken_mapping = {
        "missing archive file": "archive_missing_file",
        "encrypted archive": "archive_encrypted",
        "extracting archive with 7z failed": "archive_extraction_failed",

        "corrupted_file": "emails_corrupted_file",
        "payload_error": "emails_payload_error",
        "missing_emlx_part": "emails_missing_emlx_part",

        "decryption failed": "pgp_decryption_failed",
        
        "extracting archive with readpst failed": "pst_extraction_failed",
        "missing pst file": "pst_missing_file",
    }

    Document = apps.get_model("snoop", "Document")

    for doc in Document.objects.all():
        if doc.broken:
            doc.broken = broken_mapping[doc.broken]
            doc.save()
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('snoop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(refactor_exceptions)
    ]
