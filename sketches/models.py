"""Django models for sketches app."""

from django.db import models
from django.urls import reverse

try:
    from blog.models import Photo
except ImportError:
    Photo = None


class Sketch(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")
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
