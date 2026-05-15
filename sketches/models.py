"""Django models for sketches app."""

from django.db import models
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
