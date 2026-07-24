from django.core.management.base import BaseCommand
from django.utils import timezone

from sketches.models import TemporarySketchMedia


class Command(BaseCommand):
    help = "Delete expired temporary sketch media records and their stored files."

    def handle(self, *args, **options):
        queryset = TemporarySketchMedia.objects.filter(expires_at__lte=timezone.now())
        count = queryset.count()
        queryset.delete()
        self.stdout.write(f"Deleted {count} expired temporary sketch media item(s).")
