from django.db import migrations
from django.utils.text import slugify


def make_photo_slugs(apps, _):
    Photo = apps.get_model("blog", "Photo")
    for photo in Photo.objects.all():
        if not photo.slug and photo.title:
            # Generate slug from title
            base_slug = slugify(photo.title)
            slug = base_slug
            counter = 1

            # Ensure uniqueness
            while Photo.objects.filter(slug=slug).exclude(pk=photo.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            photo.slug = slug
            photo.save()
            print("Made slug for photo", photo.title, "=", photo.slug)


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_photo_slug"),
    ]

    operations = [
        migrations.RunPython(make_photo_slugs, reverse_code=migrations.RunPython.noop),
    ]
