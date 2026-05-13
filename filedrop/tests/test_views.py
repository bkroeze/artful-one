import os
import pytest
from datetime import timedelta
from unittest.mock import patch
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from filedrop.models import Drop, Token, DownloadLog


@pytest.fixture
def test_file(tmp_path):
    """Create a temporary test file."""
    test_dir = tmp_path / "filedrop"
    test_dir.mkdir()
    test_file = test_dir / "test-document.pdf"
    test_file.write_text("Test file content")
    return str(test_file)


@pytest.fixture
def drop_with_file(test_file):
    """Create a drop pointing to the test file."""
    filename = os.path.basename(test_file)
    base_dir = os.path.dirname(test_file)

    with patch.object(settings, "FILEDROP_BASE_DIR", base_dir):
        drop = Drop.objects.create(shortname="test-doc", filename=filename)
        yield drop


@pytest.mark.django_db
def test_download_success(client, drop_with_file, test_file):
    """Test successful download with valid token."""
    base_dir = os.path.dirname(test_file)

    token = Token.objects.create(
        drop=drop_with_file,
        token_value="valid-token-123",
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5,
    )

    with patch.object(settings, "FILEDROP_BASE_DIR", base_dir):
        url = reverse(
            "filedrop:download", kwargs={"shortname": drop_with_file.shortname}
        )
        response = client.get(url, {"token": "valid-token-123"})

        assert response.status_code == 200
        assert response["Content-Type"] == "application/pdf"
        assert "attachment" in response.get("Content-Disposition", "")

        # Check usage was incremented
        token.refresh_from_db()
        assert token.usage_count == 1

        # Check log was created
        assert DownloadLog.objects.filter(token=token).count() == 1
        log = DownloadLog.objects.first()
        assert log.success is True


@pytest.mark.django_db
def test_download_invalid_token(client, drop_with_file):
    """Test download with invalid token."""
    base_dir = os.path.dirname(os.path.dirname(drop_with_file.get_full_path()))

    with patch.object(settings, "FILEDROP_BASE_DIR", base_dir):
        url = reverse(
            "filedrop:download", kwargs={"shortname": drop_with_file.shortname}
        )
        response = client.get(url, {"token": "invalid-token"})

        assert response.status_code == 403


@pytest.mark.django_db
def test_download_expired_token(client, drop_with_file, test_file):
    """Test download with expired token."""
    base_dir = os.path.dirname(test_file)

    Token.objects.create(
        drop=drop_with_file,
        token_value="expired-token",
        expiration_date=timezone.now() - timedelta(days=1),
        usage_limit=5,
    )

    with patch.object(settings, "FILEDROP_BASE_DIR", base_dir):
        url = reverse(
            "filedrop:download", kwargs={"shortname": drop_with_file.shortname}
        )
        response = client.get(url, {"token": "expired-token"})

        assert response.status_code == 403


@pytest.mark.django_db
def test_download_usage_exceeded(client, drop_with_file, test_file):
    """Test download when usage limit exceeded."""
    base_dir = os.path.dirname(test_file)

    Token.objects.create(
        drop=drop_with_file,
        token_value="exceeded-token",
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=2,
        usage_count=2,
    )

    with patch.object(settings, "FILEDROP_BASE_DIR", base_dir):
        url = reverse(
            "filedrop:download", kwargs={"shortname": drop_with_file.shortname}
        )
        response = client.get(url, {"token": "exceeded-token"})

        assert response.status_code == 403


@pytest.mark.django_db
def test_download_file_not_found(client, drop_with_file):
    """Test download when file doesn't exist on filesystem."""
    base_dir = os.path.dirname(os.path.dirname(drop_with_file.get_full_path()))

    Token.objects.create(
        drop=drop_with_file,
        token_value="valid-token",
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5,
    )

    # Delete the file
    if os.path.exists(drop_with_file.get_full_path()):
        os.remove(drop_with_file.get_full_path())

    with patch.object(settings, "FILEDROP_BASE_DIR", base_dir):
        url = reverse(
            "filedrop:download", kwargs={"shortname": drop_with_file.shortname}
        )
        response = client.get(url, {"token": "valid-token"})

        assert response.status_code == 404


@pytest.mark.django_db
def test_download_missing_token(client, drop_with_file):
    """Test download without token parameter."""
    base_dir = os.path.dirname(os.path.dirname(drop_with_file.get_full_path()))

    with patch.object(settings, "FILEDROP_BASE_DIR", base_dir):
        url = reverse(
            "filedrop:download", kwargs={"shortname": drop_with_file.shortname}
        )
        response = client.get(url)

        assert response.status_code == 400


@pytest.mark.django_db
def test_download_nonexistent_drop(client):
    """Test download for non-existent drop."""
    url = reverse("filedrop:download", kwargs={"shortname": "nonexistent"})
    response = client.get(url, {"token": "some-token"})

    assert response.status_code == 404


@pytest.mark.django_db
def test_path_traversal_protection(client):
    """Test that path traversal attacks are blocked."""
    drop = Drop.objects.create(shortname="malicious", filename="../../../etc/passwd")

    Token.objects.create(
        drop=drop,
        token_value="valid-token",
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5,
    )

    url = reverse("filedrop:download", kwargs={"shortname": drop.shortname})
    response = client.get(url, {"token": "valid-token"})

    assert response.status_code in [403, 404]
