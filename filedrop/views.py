import os
import mimetypes
from django.http import (
    FileResponse,
    HttpResponseForbidden,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import View
from .models import Drop, Token


class FileDownloadView(View):
    """Handle secure file downloads with token authentication."""

    def get(self, request, shortname):
        # Get token from query parameter
        token_value = request.GET.get("token")
        if not token_value:
            return HttpResponseBadRequest("Token is required")

        # Get the drop
        drop = get_object_or_404(Drop, shortname=shortname)

        # Get and validate token
        try:
            token = Token.objects.get(drop=drop, token_value=token_value)
        except Token.DoesNotExist:
            self._log_attempt(request, None, False, "Invalid token")
            return HttpResponseForbidden("Invalid token")

        if not token.is_valid():
            if not token.is_active:
                self._log_attempt(request, token, False, "Token is inactive")
                return HttpResponseForbidden("Token is inactive")
            elif timezone.now() > token.expiration_date:
                self._log_attempt(request, token, False, "Token has expired")
                return HttpResponseForbidden("Token has expired")
            elif token.usage_count >= token.usage_limit:
                self._log_attempt(request, token, False, "Usage limit exceeded")
                return HttpResponseForbidden("Usage limit exceeded")

        # Verify file exists and is accessible
        try:
            file_path = drop.get_full_path()
        except ValueError as e:
            self._log_attempt(request, token, False, f"Invalid filename: {str(e)}")
            return HttpResponseForbidden("Invalid filename")

        if not os.path.exists(file_path):
            self._log_attempt(request, token, False, "File not found on server")
            return HttpResponseNotFound("File not found")

        if not os.path.isfile(file_path):
            self._log_attempt(request, token, False, "Path is not a file")
            return HttpResponseNotFound("File not found")

        # Increment usage counter
        token.increment_usage()

        # Log successful download
        self._log_attempt(request, token, True)

        # Determine content type
        content_type, _ = mimetypes.guess_type(file_path)
        if not content_type:
            content_type = "application/octet-stream"

        # Create response with proper headers for download
        response = FileResponse(
            open(file_path, "rb"),
            content_type=content_type,
            as_attachment=True,
            filename=drop.filename,
        )

        return response

    def _log_attempt(self, request, token, success, error_message=""):
        """Log download attempt for audit purposes."""
        from .models import DownloadLog

        # Only log if we have a valid token (can't log without a token reference)
        if token is None:
            return

        # Get client IP
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(",")[0].strip()
        else:
            ip_address = request.META.get("REMOTE_ADDR")

        # Get user agent
        user_agent = request.META.get("HTTP_USER_AGENT", "")

        DownloadLog.objects.create(
            token=token,
            ip_address=ip_address,
            user_agent=user_agent,
            success=success,
            error_message=error_message,
        )
