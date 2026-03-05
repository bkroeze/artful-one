import pytest
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from filedrop.models import Drop, Token


@pytest.mark.django_db
def test_admin_drop_list_view(client):
    admin_user = get_user_model().objects.create_superuser(
        "admin", "admin@test.com", "password"
    )
    client.force_login(admin_user)

    Drop.objects.create(shortname="test", filename="file.pdf")

    response = client.get(reverse("admin:filedrop_drop_changelist"))
    assert response.status_code == 200
    assert b"test" in response.content


@pytest.mark.django_db
def test_admin_token_inline_display(client):
    admin_user = get_user_model().objects.create_superuser(
        "admin", "admin@test.com", "password"
    )
    client.force_login(admin_user)

    drop = Drop.objects.create(shortname="test", filename="file.pdf")
    Token.objects.create(
        drop=drop,
        token_value="abc123",
        expiration_date=timezone.now() + timedelta(days=7),
        usage_limit=5,
    )

    response = client.get(reverse("admin:filedrop_drop_change", args=[drop.pk]))
    assert response.status_code == 200
