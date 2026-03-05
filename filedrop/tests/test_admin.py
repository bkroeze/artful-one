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


@pytest.mark.django_db
def test_admin_generate_token_post(client):
    """Test POST request to generate token creates a token."""
    admin_user = get_user_model().objects.create_superuser(
        "admin", "admin@test.com", "password"
    )
    client.force_login(admin_user)

    drop = Drop.objects.create(shortname="test", filename="file.pdf")

    response = client.post(
        reverse("admin:filedrop_drop_generate_token", args=[drop.pk]),
        {"expiration_days": 30, "usage_limit": 10},
    )

    assert response.status_code == 302  # Redirect after success
    assert Token.objects.filter(drop=drop).count() == 1
    token = Token.objects.get(drop=drop)
    assert token.usage_limit == 10


@pytest.mark.django_db
def test_admin_generate_token_permission_denied(client):
    """Test staff users without change_drop permission cannot generate tokens."""
    # Create a staff user without filedrop.change_drop permission
    staff_user = get_user_model().objects.create_user(
        "staff", "staff@test.com", "password", is_staff=True
    )
    client.force_login(staff_user)

    drop = Drop.objects.create(shortname="test", filename="file.pdf")

    response = client.get(reverse("admin:filedrop_drop_generate_token", args=[drop.pk]))

    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_generate_token_not_found(client):
    """Test 404 response for non-existent drop."""
    admin_user = get_user_model().objects.create_superuser(
        "admin", "admin@test.com", "password"
    )
    client.force_login(admin_user)

    response = client.get(reverse("admin:filedrop_drop_generate_token", args=[99999]))

    assert response.status_code == 404
