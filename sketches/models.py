"""Django models for sketches app."""

import hashlib
import os
import secrets
import uuid
from datetime import timedelta

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError, models, transaction
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone

from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import reverse

try:
    from blog.models import Photo
except ImportError:
    Photo = None


class Sketch(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")
    visible = models.BooleanField(default=True)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sketches",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Sketch"
        verbose_name_plural = "Sketches"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sketch_detail", kwargs={"slug": self.slug})


class Animation(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    thumbnail = models.ForeignKey(
        Photo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="animations",
    )
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Animation"
        verbose_name_plural = "Animations"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("animation_detail", kwargs={"slug": self.slug})

    @property
    def template_name(self):
        return f"animations/{self.slug}.html"

    def has_template(self):
        try:
            get_template(self.template_name)
        except TemplateDoesNotExist:
            return False
        return True


class WorkingSketch(models.Model):
    class SketchType(models.TextChoices):
        D3 = "d3", "D3"
        PROCESSING = "processing", "Processing"
        RAW = "raw", "Raw"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="working_sketches",
    )
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    sketch_type = models.CharField(max_length=10, choices=SketchType.choices)
    startup_js = models.TextField(blank=True, default="")
    div_html = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Working sketch"
        verbose_name_plural = "Working sketches"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("working_sketch_detail", kwargs={"slug": self.slug})


class SketchToken(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sketch_tokens",
    )
    name = models.CharField(max_length=255)
    prefix = models.CharField(max_length=16, unique=True, editable=False)
    digest = models.CharField(max_length=64, unique=True, editable=False)
    active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["user_id", "name"]
        verbose_name = "Sketch token"
        verbose_name_plural = "Sketch tokens"

    def __str__(self):
        return f"{self.user}: {self.name}"

    @staticmethod
    def _new_raw_token():
        return secrets.token_urlsafe(32)

    @staticmethod
    def _digest(raw_token):
        return hashlib.sha256(raw_token.encode("utf-8")).hexdigest()

    @classmethod
    def issue(cls, user, name, expires_at=None):
        while True:
            raw_token = cls._new_raw_token()
            prefix = raw_token[:16]
            if cls.objects.filter(prefix=prefix).exists():
                continue

            try:
                with transaction.atomic():
                    token = cls.objects.create(
                        user=user,
                        name=name,
                        prefix=prefix,
                        digest=cls._digest(raw_token),
                        expires_at=expires_at,
                    )
            except IntegrityError:
                if cls.objects.filter(prefix=prefix).exists():
                    continue
                raise
            return token, raw_token

    def matches(self, raw_token):
        if not isinstance(raw_token, str):
            return False
        digest_matches = secrets.compare_digest(
            self.digest,
            self._digest(raw_token),
        )
        is_current = self.expires_at is None or self.expires_at > timezone.now()
        return digest_matches and self.active and is_current


def default_temporary_media_expiry():
    return timezone.now() + timedelta(days=7)


def temporary_sketch_media_upload_to(instance, filename):
    basename = os.path.basename(filename.replace("\\", "/"))
    return f"sketches/temporary/{instance.owner_id}/{instance.pk}/{basename}"


temporary_sketch_media_storage = FileSystemStorage(location=settings.SKETCHY_MEDIA_ROOT)


class TemporarySketchMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="temporary_sketch_media",
    )
    sketch = models.ForeignKey(
        WorkingSketch,
        on_delete=models.SET_NULL,
        related_name="temporary_media",
        null=True,
        blank=True,
    )
    file = models.FileField(
        upload_to=temporary_sketch_media_upload_to,
        storage=temporary_sketch_media_storage,
        max_length=500,
    )
    original_name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255, blank=True, default="")
    size = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=default_temporary_media_expiry)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Temporary sketch media"
        verbose_name_plural = "Temporary sketch media"

    def __str__(self):
        return self.original_name

    @property
    def reference(self):
        return f"sketchy-media://{self.pk}"

    @property
    def is_expired(self):
        return self.expires_at <= timezone.now()


@receiver(post_delete, sender=TemporarySketchMedia)
def delete_temporary_sketch_media_file(sender, instance, using, **kwargs):
    if instance.file and instance.file.name:
        storage = instance.file.storage
        name = instance.file.name
        transaction.on_commit(lambda: storage.delete(name), using=using)
