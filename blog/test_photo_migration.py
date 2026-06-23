import importlib

import pytest
from django.apps import apps

from blog.models import Photo


@pytest.mark.django_db
def test_photo_image_migration_prefers_staticroot_uploads(settings, tmp_path):
    migration = importlib.import_module("blog.migrations.0014_alter_photo_image")
    base_dir = tmp_path / "project"
    static_root = tmp_path / "staticfiles"
    media_root = tmp_path / "media"
    settings.BASE_DIR = str(base_dir)
    settings.STATIC_ROOT = str(static_root)
    settings.MEDIA_ROOT = str(media_root)

    photo = Photo.objects.create(title="Static Upload")
    Photo.objects.filter(pk=photo.pk).update(image="photos/static-first.avif")
    (static_root / "photos" / "static-first").mkdir(parents=True)
    (base_dir / "photos" / "static-first").mkdir(parents=True)
    (static_root / "photos" / "static-first.avif").write_text("static original")
    (static_root / "photos" / "static-first" / "100w.avif").write_text(
        "static rendition"
    )
    (base_dir / "photos" / "static-first.avif").write_text("legacy original")
    (base_dir / "photos" / "static-first" / "100w.avif").write_text("legacy rendition")

    migration.copy_existing_photo_files_to_media(apps, None)

    assert (media_root / "photos" / "static-first.avif").read_text() == (
        "static original"
    )
    assert (media_root / "photos" / "static-first" / "100w.avif").read_text() == (
        "static rendition"
    )


@pytest.mark.django_db
def test_photo_image_migration_falls_back_to_checked_in_photos(settings, tmp_path):
    migration = importlib.import_module("blog.migrations.0014_alter_photo_image")
    base_dir = tmp_path / "project"
    static_root = tmp_path / "staticfiles"
    media_root = tmp_path / "media"
    settings.BASE_DIR = str(base_dir)
    settings.STATIC_ROOT = str(static_root)
    settings.MEDIA_ROOT = str(media_root)

    photo = Photo.objects.create(title="Legacy Photo")
    Photo.objects.filter(pk=photo.pk).update(image="photos/legacy-only.avif")
    (base_dir / "photos" / "legacy-only").mkdir(parents=True)
    (base_dir / "photos" / "legacy-only.avif").write_text("legacy original")
    (base_dir / "photos" / "legacy-only" / "100w.avif").write_text("legacy rendition")

    migration.copy_existing_photo_files_to_media(apps, None)

    assert (media_root / "photos" / "legacy-only.avif").read_text() == (
        "legacy original"
    )
    assert (media_root / "photos" / "legacy-only" / "100w.avif").read_text() == (
        "legacy rendition"
    )
