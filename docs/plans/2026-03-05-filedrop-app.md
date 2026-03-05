# Filedrop App Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a Django app for secure file downloads via token-authenticated endpoints with expiration and usage limits.

**Architecture:** 
- Models: Drop (file metadata), Token (access credentials with limits), DownloadLog (audit trail)
- One Drop can have multiple Tokens (one-to-many relationship)
- Admin interface with token generation button and download URL display
- Secure download endpoint with path traversal protection and comprehensive logging

**Tech Stack:** Django, Django Admin (custom actions), FileResponse for streaming

---

## Task 1: Create Django App Structure

**Files:**
- Create: `filedrop/__init__.py`
- Create: `filedrop/apps.py`
- Create: `filedrop/admin.py`
- Create: `filedrop/models.py`
- Create: `filedrop/views.py`
- Create: `filedrop/urls.py`
- Modify: `config/settings.py` (add app to INSTALLED_APPS)

**Step 1: Create app directory and files**

Create `filedrop/__init__.py`:
```python
default_app_config = 'filedrop.apps.FiledropConfig'
```

Create `filedrop/apps.py`:
```python
from django.apps import AppConfig


class FiledropConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filedrop'
    verbose_name = 'File Drop'
```

**Step 2: Add to settings**

Modify `config/settings.py` to add 'filedrop' to INSTALLED_APPS.

**Step 3: Verify app loads**

Run: `uv run manage.py check`
Expected: System check identified no issues

**Step 4: Commit**

```bash
git add filedrop/ config/settings.py
git commit -m "feat: create filedrop app structure"
```

---

## Task 2: Create Models (Drop, Token, DownloadLog)

**Files:**
- Create: `filedrop/models.py`

**Step 1: Write model tests first**

Create test file `filedrop/tests/test_models.py`:
```python
import pytest
from datetime import timedelta
from django.utils import timezone
from filedrop.models import Drop, Token, DownloadLog


@pytest.mark.django_db
def test_drop_creation():
    drop = Drop.objects.create(
        shortname='test-file',
        filename='document.pdf'
    )
    assert drop.shortname == 'test-file'
    assert drop.filename == 'document.pdf'
    assert drop.created_at is not None


@pytest.mark.django_db
def test_token_creation():
    drop = Drop.objects.create(shortname='test', filename='file.pdf')
    token = Token.objects.create(
        drop=drop,
        token_value='abc123',
        expiration_date=timezone.now() + timedelta(days=7),
        usage_limit=5
    )
    assert token.drop == drop
    assert token.token_value == 'abc123'
    assert token.usage_limit == 5
    assert token.usage_count == 0
    assert token.is_active is True


@pytest.mark.django_db
def test_token_is_valid():
    drop = Drop.objects.create(shortname='test', filename='file.pdf')
    
    # Valid token
    valid_token = Token.objects.create(
        drop=drop,
        token_value='valid',
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5
    )
    assert valid_token.is_valid() is True
    
    # Expired token
    expired_token = Token.objects.create(
        drop=drop,
        token_value='expired',
        expiration_date=timezone.now() - timedelta(days=1),
        usage_limit=5
    )
    assert expired_token.is_valid() is False
    
    # Usage exceeded
    exceeded_token = Token.objects.create(
        drop=drop,
        token_value='exceeded',
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=2,
        usage_count=2
    )
    assert exceeded_token.is_valid() is False
    
    # Inactive token
    inactive_token = Token.objects.create(
        drop=drop,
        token_value='inactive',
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5,
        is_active=False
    )
    assert inactive_token.is_valid() is False


@pytest.mark.django_db
def test_download_log_creation():
    drop = Drop.objects.create(shortname='test', filename='file.pdf')
    token = Token.objects.create(
        drop=drop,
        token_value='token123',
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5
    )
    log = DownloadLog.objects.create(
        token=token,
        ip_address='192.168.1.1',
        user_agent='Mozilla/5.0',
        success=True
    )
    assert log.token == token
    assert log.ip_address == '192.168.1.1'
    assert log.success is True
```

**Step 2: Run tests to verify they fail**

Run: `uv run pytest filedrop/tests/test_models.py -v`
Expected: FAIL with model import errors

**Step 3: Implement models**

Create `filedrop/models.py`:
```python
import os
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


class Drop(models.Model):
    shortname = models.SlugField(max_length=100, unique=True, db_index=True)
    filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.shortname} ({self.filename})"
    
    def get_full_path(self):
        """Get full filesystem path with security validation."""
        base_dir = getattr(settings, 'FILEDROP_BASE_DIR', None)
        if not base_dir:
            raise ValueError("FILEDROP_BASE_DIR not configured in settings")
        
        # Normalize and validate path
        base_path = os.path.abspath(os.path.normpath(base_dir))
        full_path = os.path.abspath(os.path.normpath(os.path.join(base_dir, self.filename)))
        
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
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, related_name='tokens')
    token_value = models.CharField(max_length=255, unique=True, db_index=True)
    expiration_date = models.DateTimeField()
    usage_limit = models.PositiveIntegerField(default=1)
    usage_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
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
        self.save(update_fields=['usage_count'])


class DownloadLog(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE, related_name='download_logs')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)
    error_message = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"Download {self.token.drop.shortname} at {self.timestamp}"
```

**Step 4: Run tests to verify they pass**

Run: `uv run pytest filedrop/tests/test_models.py -v`
Expected: All 4 tests PASS

**Step 5: Commit**

```bash
git add filedrop/models.py filedrop/tests/test_models.py
git commit -m "feat: add Drop, Token, and DownloadLog models with validation"
```

---

## Task 3: Create and Run Migrations

**Files:**
- Create: `filedrop/migrations/0001_initial.py`

**Step 1: Create migrations**

Run: `uv run manage.py makemigrations filedrop`
Expected: Creates 0001_initial.py

**Step 2: Apply migrations**

Run: `uv run manage.py migrate`
Expected: Applied filedrop.0001_initial

**Step 3: Commit**

```bash
git add filedrop/migrations/
git commit -m "chore: add initial filedrop migrations"
```

---

## Task 4: Configure FILEDROP_BASE_DIR Setting

**Files:**
- Modify: `config/settings.py`

**Step 1: Add FILEDROP_BASE_DIR setting**

Add to `config/settings.py` after other path configurations:
```python
# Filedrop configuration
FILEDROP_BASE_DIR = os.path.join(BASE_DIR, 'filedrop_files')
```

Also ensure the directory exists by adding to settings or documenting.

**Step 2: Create the directory**

Run: `mkdir -p filedrop_files`

**Step 3: Verify settings load**

Run: `uv run manage.py check`
Expected: System check identified no issues

**Step 4: Commit**

```bash
git add config/settings.py filedrop_files/.gitkeep
git commit -m "chore: configure FILEDROP_BASE_DIR setting"
```

---

## Task 5: Create Custom Admin with Token Generation

**Files:**
- Create: `filedrop/admin.py`
- Create: `filedrop/forms.py`

**Step 1: Write admin tests**

Create `filedrop/tests/test_admin.py`:
```python
import pytest
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from filedrop.models import Drop, Token


@pytest.mark.django_db
def test_admin_drop_list_view(client):
    admin_user = get_user_model().objects.create_superuser('admin', 'admin@test.com', 'password')
    client.force_login(admin_user)
    
    Drop.objects.create(shortname='test', filename='file.pdf')
    
    response = client.get(reverse('admin:filedrop_drop_changelist'))
    assert response.status_code == 200
    assert b'test' in response.content


@pytest.mark.django_db
def test_admin_token_inline_display(client):
    admin_user = get_user_model().objects.create_superuser('admin', 'admin@test.com', 'password')
    client.force_login(admin_user)
    
    drop = Drop.objects.create(shortname='test', filename='file.pdf')
    Token.objects.create(
        drop=drop,
        token_value='abc123',
        expiration_date=timezone.now() + timedelta(days=7),
        usage_limit=5
    )
    
    response = client.get(reverse('admin:filedrop_drop_change', args=[drop.pk]))
    assert response.status_code == 200
```

**Step 2: Run tests (should fail)**

Run: `uv run pytest filedrop/tests/test_admin.py -v`
Expected: FAIL (admin not configured)

**Step 3: Implement admin**

Create `filedrop/forms.py`:
```python
from django import forms
from .models import Token


class TokenGenerationForm(forms.Form):
    """Form for generating new tokens."""
    expiration_days = forms.IntegerField(
        min_value=1,
        max_value=365,
        initial=30,
        label='Expires in (days)',
        help_text='Number of days until token expires'
    )
    usage_limit = forms.IntegerField(
        min_value=1,
        max_value=1000,
        initial=10,
        label='Usage limit',
        help_text='Maximum number of downloads allowed'
    )
```

Create `filedrop/admin.py`:
```python
import uuid
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect, render
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from .models import Drop, Token, DownloadLog
from .forms import TokenGenerationForm


class TokenInline(admin.TabularInline):
    model = Token
    extra = 0
    readonly_fields = ['token_value', 'created_at', 'is_valid_display', 'usage_display', 'download_url']
    fields = ['token_value', 'expiration_date', 'usage_limit', 'usage_count', 'is_active', 'is_valid_display', 'usage_display', 'download_url']
    
    def is_valid_display(self, obj):
        if obj.pk:
            return 'Yes' if obj.is_valid() else 'No'
        return '-'
    is_valid_display.short_description = 'Valid'
    
    def usage_display(self, obj):
        if obj.pk:
            return f"{obj.usage_count} / {obj.usage_limit}"
        return '-'
    usage_display.short_description = 'Usage'
    
    def download_url(self, obj):
        if obj.pk:
            from django.urls import reverse
            from django.utils.html import format_html
            url = reverse('filedrop:download', kwargs={'shortname': obj.drop.shortname})
            full_url = f"{url}?token={obj.token_value}"
            return format_html('<a href="{}" target="_blank">{}</a>', full_url, full_url)
        return '-'
    download_url.short_description = 'Download URL'
    
    def has_add_permission(self, request, obj=None):
        # Disable default add - we use custom button instead
        return False


class DownloadLogInline(admin.TabularInline):
    model = DownloadLog
    extra = 0
    readonly_fields = ['timestamp', 'ip_address', 'success', 'error_message']
    fields = ['timestamp', 'ip_address', 'success', 'error_message']
    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Drop)
class DropAdmin(admin.ModelAdmin):
    list_display = ['shortname', 'filename', 'file_exists', 'created_at', 'token_count']
    list_filter = ['created_at']
    search_fields = ['shortname', 'filename']
    inlines = [TokenInline]
    readonly_fields = ['created_at', 'file_exists']
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:drop_id>/generate-token/',
                self.admin_site.admin_view(self.generate_token_view),
                name='filedrop_drop_generate_token',
            ),
        ]
        return custom_urls + urls
    
    def generate_token_view(self, request, drop_id):
        drop = Drop.objects.get(pk=drop_id)
        
        if request.method == 'POST':
            form = TokenGenerationForm(request.POST)
            if form.is_valid():
                expiration_days = form.cleaned_data['expiration_days']
                usage_limit = form.cleaned_data['usage_limit']
                
                token = Token.objects.create(
                    drop=drop,
                    token_value=str(uuid.uuid4()),
                    expiration_date=timezone.now() + timedelta(days=expiration_days),
                    usage_limit=usage_limit
                )
                
                messages.success(
                    request,
                    f"Token generated successfully: {token.token_value}"
                )
                return redirect('admin:filedrop_drop_change', drop_id)
        else:
            form = TokenGenerationForm()
        
        context = {
            'title': f'Generate Token for {drop.shortname}',
            'form': form,
            'drop': drop,
            'opts': self.model._meta,
            **self.admin_site.each_context(request),
        }
        return render(request, 'admin/filedrop/drop/generate_token.html', context)
    
    def token_count(self, obj):
        return obj.tokens.count()
    token_count.short_description = 'Tokens'


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['drop', 'token_value_short', 'expiration_date', 'usage_display', 'is_active', 'is_valid_display', 'created_at']
    list_filter = ['is_active', 'expiration_date', 'created_at']
    search_fields = ['drop__shortname', 'token_value']
    readonly_fields = ['token_value', 'created_at', 'is_valid_display', 'download_url']
    
    def token_value_short(self, obj):
        return f"{obj.token_value[:16]}..."
    token_value_short.short_description = 'Token'
    
    def is_valid_display(self, obj):
        return 'Yes' if obj.is_valid() else 'No'
    is_valid_display.short_description = 'Valid'
    
    def usage_display(self, obj):
        return f"{obj.usage_count} / {obj.usage_limit}"
    usage_display.short_description = 'Usage'
    
    def download_url(self, obj):
        from django.urls import reverse
        from django.utils.html import format_html
        url = reverse('filedrop:download', kwargs={'shortname': obj.drop.shortname})
        full_url = f"{url}?token={obj.token_value}"
        return format_html('<a href="{}" target="_blank">{}</a>', full_url, full_url)
    download_url.short_description = 'Download URL'


@admin.register(DownloadLog)
class DownloadLogAdmin(admin.ModelAdmin):
    list_display = ['token', 'ip_address', 'timestamp', 'success']
    list_filter = ['success', 'timestamp']
    search_fields = ['token__drop__shortname', 'ip_address']
    readonly_fields = ['token', 'ip_address', 'user_agent', 'timestamp', 'success', 'error_message']
    
    def has_add_permission(self, request):
        return False
```

**Step 4: Create admin template for token generation**

Create `filedrop/templates/admin/filedrop/drop/generate_token.html`:
```html
{% extends "admin/base_site.html" %}
{% load i18n admin_urls static %}

{% block content %}
<div id="content-main">
    <h1>Generate New Token for {{ drop.shortname }}</h1>
    
    <p>Current file: <strong>{{ drop.filename }}</strong></p>
    
    <form method="post">
        {% csrf_token %}
        <fieldset class="module aligned">
            {% for field in form %}
            <div class="form-row">
                {{ field.errors }}
                <div>
                    <label for="{{ field.id_for_label }}">{{ field.label }}:</label>
                    {{ field }}
                    {% if field.help_text %}
                    <p class="help">{{ field.help_text }}</p>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </fieldset>
        
        <div class="submit-row">
            <input type="submit" value="Generate Token" class="default" name="_generate">
            <a href="{% url 'admin:filedrop_drop_change' drop.id %}" class="button cancel-link" style="margin-left: 10px;">Cancel</a>
        </div>
    </form>
</div>
{% endblock %}
```

**Step 5: Run tests to verify they pass**

Run: `uv run pytest filedrop/tests/test_admin.py -v`
Expected: Tests PASS

**Step 6: Commit**

```bash
git add filedrop/admin.py filedrop/forms.py filedrop/templates/
git commit -m "feat: add admin interface with token generation"
```

---

## Task 6: Add "Generate Token" Button to Drop Change Page

**Files:**
- Create: `filedrop/templates/admin/filedrop/drop/change_form.html`

**Step 1: Override admin change form template**

Create `filedrop/templates/admin/filedrop/drop/change_form.html`:
```html
{% extends "admin/change_form.html" %}
{% load i18n admin_urls %}

{% block object-tools-items %}
    <li>
        <a href="{% url 'admin:filedrop_drop_generate_token' original.pk %}" class="historylink" style="background: #417690;">Generate Token</a>
    </li>
    {{ block.super }}
{% endblock %}
```

**Step 2: Verify template loads**

Access Django admin, navigate to a Drop, verify "Generate Token" button appears.

**Step 3: Commit**

```bash
git add filedrop/templates/admin/filedrop/drop/change_form.html
git commit -m "feat: add generate token button to admin change form"
```

---

## Task 7: Create Download View

**Files:**
- Create: `filedrop/views.py`
- Create: `filedrop/tests/test_views.py`

**Step 1: Write view tests**

Create `filedrop/tests/test_views.py`:
```python
import os
import pytest
from datetime import timedelta
from unittest.mock import patch
from django.urls import reverse
from django.utils import timezone
from django.http import Http404
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
    
    with patch.object(settings, 'FILEDROP_BASE_DIR', base_dir):
        drop = Drop.objects.create(
            shortname='test-doc',
            filename=filename
        )
        yield drop


@pytest.mark.django_db
def test_download_success(client, drop_with_file, test_file):
    """Test successful download with valid token."""
    base_dir = os.path.dirname(test_file)
    
    token = Token.objects.create(
        drop=drop_with_file,
        token_value='valid-token-123',
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5
    )
    
    with patch.object(settings, 'FILEDROP_BASE_DIR', base_dir):
        url = reverse('filedrop:download', kwargs={'shortname': drop_with_file.shortname})
        response = client.get(url, {'token': 'valid-token-123'})
        
        assert response.status_code == 200
        assert response['Content-Type'] == 'application/pdf'
        assert 'attachment' in response.get('Content-Disposition', '')
        
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
    
    with patch.object(settings, 'FILEDROP_BASE_DIR', base_dir):
        url = reverse('filedrop:download', kwargs={'shortname': drop_with_file.shortname})
        response = client.get(url, {'token': 'invalid-token'})
        
        assert response.status_code == 403


@pytest.mark.django_db
def test_download_expired_token(client, drop_with_file, test_file):
    """Test download with expired token."""
    base_dir = os.path.dirname(test_file)
    
    token = Token.objects.create(
        drop=drop_with_file,
        token_value='expired-token',
        expiration_date=timezone.now() - timedelta(days=1),
        usage_limit=5
    )
    
    with patch.object(settings, 'FILEDROP_BASE_DIR', base_dir):
        url = reverse('filedrop:download', kwargs={'shortname': drop_with_file.shortname})
        response = client.get(url, {'token': 'expired-token'})
        
        assert response.status_code == 403
        assert b'expired' in response.content.lower() or b'invalid' in response.content.lower()


@pytest.mark.django_db
def test_download_usage_exceeded(client, drop_with_file, test_file):
    """Test download when usage limit exceeded."""
    base_dir = os.path.dirname(test_file)
    
    token = Token.objects.create(
        drop=drop_with_file,
        token_value='exceeded-token',
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=2,
        usage_count=2
    )
    
    with patch.object(settings, 'FILEDROP_BASE_DIR', base_dir):
        url = reverse('filedrop:download', kwargs={'shortname': drop_with_file.shortname})
        response = client.get(url, {'token': 'exceeded-token'})
        
        assert response.status_code == 403
        assert b'limit' in response.content.lower() or b'exceeded' in response.content.lower()


@pytest.mark.django_db
def test_download_file_not_found(client, drop_with_file):
    """Test download when file doesn't exist on filesystem."""
    base_dir = os.path.dirname(os.path.dirname(drop_with_file.get_full_path()))
    
    token = Token.objects.create(
        drop=drop_with_file,
        token_value='valid-token',
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5
    )
    
    # Delete the file
    if os.path.exists(drop_with_file.get_full_path()):
        os.remove(drop_with_file.get_full_path())
    
    with patch.object(settings, 'FILEDROP_BASE_DIR', base_dir):
        url = reverse('filedrop:download', kwargs={'shortname': drop_with_file.shortname})
        response = client.get(url, {'token': 'valid-token'})
        
        assert response.status_code == 404


@pytest.mark.django_db
def test_download_missing_token(client, drop_with_file):
    """Test download without token parameter."""
    base_dir = os.path.dirname(os.path.dirname(drop_with_file.get_full_path()))
    
    with patch.object(settings, 'FILEDROP_BASE_DIR', base_dir):
        url = reverse('filedrop:download', kwargs={'shortname': drop_with_file.shortname})
        response = client.get(url)
        
        assert response.status_code == 400
        assert b'token' in response.content.lower()


@pytest.mark.django_db
def test_download_nonexistent_drop(client):
    """Test download for non-existent drop."""
    url = reverse('filedrop:download', kwargs={'shortname': 'nonexistent'})
    response = client.get(url, {'token': 'some-token'})
    
    assert response.status_code == 404


@pytest.mark.django_db
def test_path_traversal_protection(client):
    """Test that path traversal attacks are blocked."""
    drop = Drop.objects.create(
        shortname='malicious',
        filename='../../../etc/passwd'
    )
    
    token = Token.objects.create(
        drop=drop,
        token_value='valid-token',
        expiration_date=timezone.now() + timedelta(days=1),
        usage_limit=5
    )
    
    url = reverse('filedrop:download', kwargs={'shortname': drop.shortname})
    response = client.get(url, {'token': 'valid-token'})
    
    assert response.status_code in [403, 404]
```

**Step 2: Run tests (should fail)**

Run: `uv run pytest filedrop/tests/test_views.py -v`
Expected: FAIL (views not implemented)

**Step 3: Implement download view**

Create `filedrop/views.py`:
```python
import os
import mimetypes
from django.http import FileResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views import View
from django.conf import settings
from .models import Drop, Token


class FileDownloadView(View):
    """Handle secure file downloads with token authentication."""
    
    def get(self, request, shortname):
        # Get token from query parameter
        token_value = request.GET.get('token')
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
            content_type = 'application/octet-stream'
        
        # Create response with proper headers for download
        response = FileResponse(
            open(file_path, 'rb'),
            content_type=content_type,
            as_attachment=True,
            filename=drop.filename
        )
        
        return response
    
    def _log_attempt(self, request, token, success, error_message=''):
        """Log download attempt for audit purposes."""
        from .models import DownloadLog
        
        # Get client IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0].strip()
        else:
            ip_address = request.META.get('REMOTE_ADDR')
        
        # Get user agent
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        DownloadLog.objects.create(
            token=token,
            ip_address=ip_address,
            user_agent=user_agent,
            success=success,
            error_message=error_message
        )
```

**Step 4: Create URL configuration**

Create `filedrop/urls.py`:
```python
from django.urls import path
from . import views

app_name = 'filedrop'

urlpatterns = [
    path('<slug:shortname>/', views.FileDownloadView.as_view(), name='download'),
]
```

**Step 5: Add to main URL configuration**

Modify `config/urls.py` to include filedrop URLs:
```python
# Add import at top
from django.urls import path, include

# Add to urlpatterns
urlpatterns = [
    # ... existing patterns ...
    path('filedrop/', include('filedrop.urls')),
]
```

**Step 6: Run tests to verify they pass**

Run: `uv run pytest filedrop/tests/test_views.py -v`
Expected: All tests PASS

**Step 7: Commit**

```bash
git add filedrop/views.py filedrop/urls.py config/urls.py filedrop/tests/test_views.py
git commit -m "feat: implement secure file download endpoint with token auth"
```

---

## Task 8: Add Missing Import and Fix Timezone

**Files:**
- Modify: `filedrop/views.py`

**Step 1: Fix imports**

Update `filedrop/views.py` to add missing import:
```python
import os
import mimetypes
from django.http import FileResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import View
from django.conf import settings
from .models import Drop, Token
```

**Step 2: Run tests**

Run: `uv run pytest filedrop/tests/ -v`
Expected: All tests PASS

**Step 3: Commit**

```bash
git add filedrop/views.py
git commit -m "fix: add missing timezone import in views"
```

---

## Task 9: Create Integration Tests

**Files:**
- Create: `filedrop/tests/test_integration.py`

**Step 1: Write integration tests**

Create `filedrop/tests/test_integration.py`:
```python
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
        
        with patch.object(settings, 'FILEDROP_BASE_DIR', str(test_dir)):
            # Step 1: Create drop via admin
            admin_user = get_user_model().objects.create_superuser(
                'admin', 'admin@test.com', 'password'
            )
            client.force_login(admin_user)
            
            # Create drop
            response = client.post(
                reverse('admin:filedrop_drop_add'),
                {
                    'shortname': 'client-project-alpha',
                    'filename': 'deliverable.pdf',
                }
            )
            assert response.status_code == 302  # Redirect after success
            
            drop = Drop.objects.get(shortname='client-project-alpha')
            assert drop.file_exists() is True
            
            # Step 2: Generate token via admin
            response = client.post(
                reverse('admin:filedrop_drop_generate_token', args=[drop.pk]),
                {
                    'expiration_days': 30,
                    'usage_limit': 5
                }
            )
            assert response.status_code == 302
            
            token = Token.objects.get(drop=drop)
            assert token.usage_limit == 5
            assert token.is_valid() is True
            
            # Step 3: Download file
            client.logout()  # Ensure we're not authenticated
            url = reverse('filedrop:download', kwargs={'shortname': drop.shortname})
            response = client.get(url, {'token': token.token_value})
            
            assert response.status_code == 200
            assert response.content == b"Client deliverable content"
            
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
        
        with patch.object(settings, 'FILEDROP_BASE_DIR', str(test_dir)):
            drop = Drop.objects.create(shortname='report', filename='report.pdf')
            
            # Create multiple tokens
            token1 = Token.objects.create(
                drop=drop,
                token_value='token-for-client-a',
                expiration_date=timezone.now() + timedelta(days=30),
                usage_limit=10
            )
            
            token2 = Token.objects.create(
                drop=drop,
                token_value='token-for-client-b',
                expiration_date=timezone.now() + timedelta(days=7),
                usage_limit=3
            )
            
            # Both tokens should work
            url = reverse('filedrop:download', kwargs={'shortname': drop.shortname})
            
            response1 = client.get(url, {'token': token1.token_value})
            assert response1.status_code == 200
            
            response2 = client.get(url, {'token': token2.token_value})
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
        
        with patch.object(settings, 'FILEDROP_BASE_DIR', str(test_dir)):
            drop1 = Drop.objects.create(shortname='drop1', filename='file1.pdf')
            drop2 = Drop.objects.create(shortname='drop2', filename='file2.pdf')
            
            token1 = Token.objects.create(
                drop=drop1,
                token_value='token1',
                expiration_date=timezone.now() + timedelta(days=30),
                usage_limit=5
            )
            
            # Token for drop1 should not work for drop2
            url = reverse('filedrop:download', kwargs={'shortname': drop2.shortname})
            response = client.get(url, {'token': token1.token_value})
            
            assert response.status_code == 403
```

**Step 2: Run integration tests**

Run: `uv run pytest filedrop/tests/test_integration.py -v`
Expected: All tests PASS

**Step 3: Commit**

```bash
git add filedrop/tests/test_integration.py
git commit -m "test: add comprehensive integration tests"
```

---

## Task 10: Create README Documentation

**Files:**
- Create: `filedrop/README.md`

**Step 1: Write documentation**

Create `filedrop/README.md`:
```markdown
# Filedrop App

Secure file download system with token-based authentication, expiration dates, and usage limits.

## Setup

1. Configure `FILEDROP_BASE_DIR` in settings (defaults to `filedrop_files/` in project root)
2. Run migrations: `uv run manage.py migrate`
3. Create files in the base directory manually

## Usage

### 1. Place File
Put files in the configured `FILEDROP_BASE_DIR` directory.

### 2. Create Drop
In Django Admin:
- Go to File Drop > Drops
- Click "Add Drop"
- Enter shortname (slug) and filename (just the filename, not path)
- Save

### 3. Generate Token
On the Drop change page:
- Click "Generate Token" button
- Set expiration (days) and usage limit
- Save
- Copy the generated token

### 4. Share Download Link
The admin shows the full download URL:
```
/filedrop/<shortname>/?token=<token-value>
```

## Security Features

- Path traversal protection (filename validation)
- Token expiration dates
- Usage limits per token
- Token deactivation
- Download logging (IP, user agent, timestamp)
- One-to-many tokens per drop (different clients get different tokens)

## URL Pattern

```
GET /filedrop/<shortname>/?token=<token>
```

Response codes:
- 200: Success (file download)
- 400: Missing token
- 403: Invalid/expired/exceeded token
- 404: Drop or file not found

## Models

### Drop
- `shortname`: Unique slug identifier
- `filename`: Name of file in base directory
- `created_at`: Timestamp

### Token
- `drop`: Foreign key to Drop
- `token_value`: Unique secure string
- `expiration_date`: When token expires
- `usage_limit`: Maximum downloads allowed
- `usage_count`: Current download count
- `is_active`: Boolean flag

### DownloadLog
- `token`: Foreign key to Token
- `ip_address`: Client IP
- `user_agent`: Client user agent
- `timestamp`: When download occurred
- `success`: Whether download succeeded
- `error_message`: Error details if failed
```

**Step 2: Commit**

```bash
git add filedrop/README.md
git commit -m "docs: add filedrop README with usage instructions"
```

---

## Task 11: Final Verification

**Step 1: Run all tests**

Run: `uv run pytest filedrop/tests/ -v`
Expected: All tests PASS

**Step 2: Run Django checks**

Run: `uv run manage.py check`
Expected: System check identified no issues

**Step 3: Verify admin loads**

Run: `uv run manage.py runserver`
- Navigate to /admin/filedrop/
- Verify Drops, Tokens, and DownloadLogs are accessible

**Step 4: Commit final changes**

```bash
git add -A
git commit -m "chore: final verification and cleanup"
```

---

## Summary

The filedrop app is now complete with:
- ✅ Secure token-based file downloads
- ✅ Path traversal protection
- ✅ Token expiration and usage limits
- ✅ One-to-many tokens per drop
- ✅ Comprehensive download logging
- ✅ Django Admin with token generation
- ✅ Full test coverage
- ✅ Documentation

**Next Steps:**
1. Place files in `filedrop_files/` directory
2. Create drops and tokens via admin
3. Share download URLs with clients
