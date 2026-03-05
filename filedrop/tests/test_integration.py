import os
import pytest
from datetime import timedelta
from unittest.mock import patch
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from filedrop.models import Drop, Token, DownloadLog


@pytest.mark.django_db
class TestFiledropIntegration:
    """Integration tests for the complete filedrop workflow."""

    def test_full_workflow(self, client, tmp_path):
        """Test the complete workflow from admin creation to download."""
        # Setup: Create test file
        test_dir = tmp_path / "filedrop"
        test_dir.mkdir()
        test_file = test_dir / "deliverable.pdf"
        test_file.write_text("Client deliverable content")

        with patch.object(settings, "FILEDROP_BASE_DIR", str(test_dir)):
            # Step 1: Create drop via admin
            admin_user = get_user_model().objects.create_superuser(
                "admin", "admin@test.com", "password"
            )
            client.force_login(admin_user)

            # Create drop (with inline formset management fields)
            response = client.post(
                reverse("admin:filedrop_drop_add"),
                {
                    "shortname": "client-project-alpha",
                    "filename": "deliverable.pdf",
                    # Inline formset management fields (required by Django admin)
                    "tokens-TOTAL_FORMS": "0",
                    "tokens-INITIAL_FORMS": "0",
                    "tokens-MIN_NUM_FORMS": "0",
                    "tokens-MAX_NUM_FORMS": "1000",
                },
            )
            assert response.status_code == 302  # Redirect after success

            drop = Drop.objects.get(shortname="client-project-alpha")
            assert drop.file_exists() is True

            # Step 2: Generate token via admin
            response = client.post(
                reverse("admin:filedrop_drop_generate_token", args=[drop.pk]),
                {"expiration_days": 30, "usage_limit": 5},
            )
            assert response.status_code == 302

            token = Token.objects.get(drop=drop)
            assert token.usage_limit == 5
            assert token.is_valid() is True

            # Step 3: Download file
            client.logout()  # Ensure we're not authenticated
            url = reverse("filedrop:download", kwargs={"shortname": drop.shortname})
            response = client.get(url, {"token": token.token_value})

            assert response.status_code == 200
            # FileResponse uses streaming_content, not content
            content = b"".join(response.streaming_content)
            assert content == b"Client deliverable content"

            # Step 4: Verify usage incremented
            token.refresh_from_db()
            assert token.usage_count == 1

            # Step 5: Verify log created
            assert DownloadLog.objects.count() == 1
            log = DownloadLog.objects.first()
            assert log.success is True
            assert log.token == token

    def test_multiple_tokens_for_one_drop(self, client, tmp_path):
        """Test that multiple tokens can exist for one drop."""
        test_dir = tmp_path / "filedrop"
        test_dir.mkdir()
        test_file = test_dir / "report.pdf"
        test_file.write_text("Report content")

        with patch.object(settings, "FILEDROP_BASE_DIR", str(test_dir)):
            drop = Drop.objects.create(shortname="report", filename="report.pdf")

            # Create multiple tokens
            token1 = Token.objects.create(
                drop=drop,
                token_value="token-for-client-a",
                expiration_date=timezone.now() + timedelta(days=30),
                usage_limit=10,
            )

            token2 = Token.objects.create(
                drop=drop,
                token_value="token-for-client-b",
                expiration_date=timezone.now() + timedelta(days=7),
                usage_limit=3,
            )

            # Both tokens should work
            url = reverse("filedrop:download", kwargs={"shortname": drop.shortname})

            response1 = client.get(url, {"token": token1.token_value})
            assert response1.status_code == 200

            response2 = client.get(url, {"token": token2.token_value})
            assert response2.status_code == 200

            # Verify independent usage tracking
            token1.refresh_from_db()
            token2.refresh_from_db()
            assert token1.usage_count == 1
            assert token2.usage_count == 1

    def test_token_isolation(self, client, tmp_path):
        """Test that tokens are isolated to their drops."""
        test_dir = tmp_path / "filedrop"
        test_dir.mkdir()

        (test_dir / "file1.pdf").write_text("File 1")
        (test_dir / "file2.pdf").write_text("File 2")

        with patch.object(settings, "FILEDROP_BASE_DIR", str(test_dir)):
            drop1 = Drop.objects.create(shortname="drop1", filename="file1.pdf")
            drop2 = Drop.objects.create(shortname="drop2", filename="file2.pdf")

            token1 = Token.objects.create(
                drop=drop1,
                token_value="token1",
                expiration_date=timezone.now() + timedelta(days=30),
                usage_limit=5,
            )

            # Token for drop1 should not work for drop2
            url = reverse("filedrop:download", kwargs={"shortname": drop2.shortname})
            response = client.get(url, {"token": token1.token_value})

            assert response.status_code == 403
