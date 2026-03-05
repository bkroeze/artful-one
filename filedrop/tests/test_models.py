import pytest
from datetime import timedelta
from django.utils import timezone
from filedrop.models import Drop, Token, DownloadLog


@pytest.mark.django_db
def test_drop_creation():
    drop = Drop.objects.create(shortname="test-file", filename="document.pdf")
    assert drop.shortname == "test-file"
    assert drop.filename == "document.pdf"
    assert drop.created_at is not None


@pytest.mark.django_db
def test_token_creation():
    drop = Drop.objects.create(shortname="test", filename="file.pdf")
    token = Token.objects.create(
        drop=drop,
        token_value="abc123",
        expiration_date=timezone.now() + timedelta(days=7),
        usage_limit=5,
    )
    assert token.drop == drop
    assert token.token_value == "abc123"
    assert token.usage_limit == 5
    assert token.usage_count == 0
    assert token.is_active is True


@pytest.mark.django_db
def test_token_is_valid():
    drop = Drop.objects.create(shortname="test", filename="file.pdf")

    # Valid token
    valid_token = Token.objects.create(
        drop=drop,
        token_value="valid",
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5,
    )
    assert valid_token.is_valid() is True

    # Expired token
    expired_token = Token.objects.create(
        drop=drop,
        token_value="expired",
        expiration_date=timezone.now() - timedelta(days=1),
        usage_limit=5,
    )
    assert expired_token.is_valid() is False

    # Usage exceeded
    exceeded_token = Token.objects.create(
        drop=drop,
        token_value="exceeded",
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=2,
        usage_count=2,
    )
    assert exceeded_token.is_valid() is False

    # Inactive token
    inactive_token = Token.objects.create(
        drop=drop,
        token_value="inactive",
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5,
        is_active=False,
    )
    assert inactive_token.is_valid() is False


@pytest.mark.django_db
def test_download_log_creation():
    drop = Drop.objects.create(shortname="test", filename="file.pdf")
    token = Token.objects.create(
        drop=drop,
        token_value="token123",
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5,
    )
    log = DownloadLog.objects.create(
        token=token, ip_address="192.168.1.1", user_agent="Mozilla/5.0", success=True
    )
    assert log.token == token
    assert log.ip_address == "192.168.1.1"
    assert log.success is True
