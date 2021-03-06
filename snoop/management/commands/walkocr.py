from django.core.management.base import BaseCommand
from django.conf import settings
from ...ocr import walk

class Command(BaseCommand):

    help = "Ingest OCRed files"

    def add_arguments(self, parser):
        parser.add_argument('tag')

    def handle(self, verbosity, tag, **options):
        walk(tag, verbose=verbosity > 0)
