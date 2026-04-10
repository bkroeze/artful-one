import os
from django.db import models
from django.conf import settings
from django.utils import timezone


class Drop(models.Model):
    shortname = models.SlugField(max_length=100, unique=True, db_index=True)
    filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.shortname} ({self.filename})"

    def get_full_path(self):
        """Get full filesystem path with security validation."""
        base_dir = getattr(settings, "FILEDROP_BASE_DIR", None)
        if not base_dir:
            raise ValueError("FILEDROP_BASE_DIR not configured in settings")

        # Normalize and validate path
        base_path = os.path.abspath(os.path.normpath(base_dir))
        full_path = os.path.abspath(
            os.path.normpath(os.path.join(base_dir, self.filename))
        )

        # Security check: ensure file is within base directory
        if not full_path.startswith(base_path):
            raise ValueError(f"Invalid filename: {self.filename}")

        return full_path

    def file_exists(self):
        """Check if the file exists on filesystem."""
        try:
            return os.path.exists(self.get_full_path())
        except ValueError:
            return False


class Token(models.Model):
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, related_name="tokens")
    token_value = models.CharField(max_length=255, unique=True, db_index=True)
    expiration_date = models.DateTimeField()
    usage_limit = models.PositiveIntegerField(default=1)
    usage_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Token for {self.drop.shortname} ({self.token_value[:8]}...)"

    def is_valid(self):
        """Check if token is valid (not expired, not exceeded usage, still active)."""
        if not self.is_active:
            return False
        if timezone.now() > self.expiration_date:
            return False
        if self.usage_count >= self.usage_limit:
            return False
        return True

    def increment_usage(self):
        """Increment usage counter."""
        self.usage_count += 1
        self.save(update_fields=["usage_count"])


class DownloadLog(models.Model):
    token = models.ForeignKey(
        Token, on_delete=models.CASCADE, related_name="download_logs"
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)
    error_message = models.TextField(blank=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Download {self.token.drop.shortname} at {self.timestamp}"
