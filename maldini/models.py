from django.db import models
from django.contrib.postgres.fields import JSONField

class Document(models.Model):
    container = models.ForeignKey('Document', null=True)
    path = models.CharField(max_length=4000)
    disk_size = models.BigIntegerField()

    class Meta:
        unique_together = ('container', 'path')

class Digest(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

class FolderMark(models.Model):
    path = models.CharField(max_length=4000, unique=True, db_index=True)

class Error(models.Model):
    document_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
