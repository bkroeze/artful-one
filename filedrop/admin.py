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
    readonly_fields = [
        "token_value",
        "created_at",
        "is_valid_display",
        "usage_display",
        "download_url",
    ]
    fields = [
        "token_value",
        "expiration_date",
        "usage_limit",
        "usage_count",
        "is_active",
        "is_valid_display",
        "usage_display",
        "download_url",
    ]

    def is_valid_display(self, obj):
        if obj.pk:
            return "Yes" if obj.is_valid() else "No"
        return "-"

    is_valid_display.short_description = "Valid"

    def usage_display(self, obj):
        if obj.pk:
            return f"{obj.usage_count} / {obj.usage_limit}"
        return "-"

    usage_display.short_description = "Usage"

    def download_url(self, obj):
        if obj.pk:
            from django.urls import reverse, NoReverseMatch
            from django.utils.html import format_html

            try:
                url = reverse(
                    "filedrop:download", kwargs={"shortname": obj.drop.shortname}
                )
                full_url = f"{url}?token={obj.token_value}"
                return format_html(
                    '<a href="{}" target="_blank">{}</a>', full_url, full_url
                )
            except NoReverseMatch:
                return "URL not available"
        return "-"

    download_url.short_description = "Download URL"

    def has_add_permission(self, request, obj=None):
        # Disable default add - we use custom button instead
        return False


class DownloadLogInline(admin.TabularInline):
    model = DownloadLog
    extra = 0
    readonly_fields = ["timestamp", "ip_address", "success", "error_message"]
    fields = ["timestamp", "ip_address", "success", "error_message"]
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Drop)
class DropAdmin(admin.ModelAdmin):
    list_display = ["shortname", "filename", "file_exists", "created_at", "token_count"]
    list_filter = ["created_at"]
    search_fields = ["shortname", "filename"]
    inlines = [TokenInline]
    readonly_fields = ["created_at", "file_exists"]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<int:drop_id>/generate-token/",
                self.admin_site.admin_view(self.generate_token_view),
                name="filedrop_drop_generate_token",
            ),
        ]
        return custom_urls + urls

    def generate_token_view(self, request, drop_id):
        drop = Drop.objects.get(pk=drop_id)

        if request.method == "POST":
            form = TokenGenerationForm(request.POST)
            if form.is_valid():
                expiration_days = form.cleaned_data["expiration_days"]
                usage_limit = form.cleaned_data["usage_limit"]

                token = Token.objects.create(
                    drop=drop,
                    token_value=str(uuid.uuid4()),
                    expiration_date=timezone.now() + timedelta(days=expiration_days),
                    usage_limit=usage_limit,
                )

                messages.success(
                    request, f"Token generated successfully: {token.token_value}"
                )
                return redirect("admin:filedrop_drop_change", drop_id)
        else:
            form = TokenGenerationForm()

        context = {
            "title": f"Generate Token for {drop.shortname}",
            "form": form,
            "drop": drop,
            "opts": self.model._meta,
            **self.admin_site.each_context(request),
        }
        return render(request, "admin/filedrop/drop/generate_token.html", context)

    def token_count(self, obj):
        return obj.tokens.count()

    token_count.short_description = "Tokens"


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = [
        "drop",
        "token_value_short",
        "expiration_date",
        "usage_display",
        "is_active",
        "is_valid_display",
        "created_at",
    ]
    list_filter = ["is_active", "expiration_date", "created_at"]
    search_fields = ["drop__shortname", "token_value"]
    readonly_fields = ["token_value", "created_at", "is_valid_display", "download_url"]

    def token_value_short(self, obj):
        return f"{obj.token_value[:16]}..."

    token_value_short.short_description = "Token"

    def is_valid_display(self, obj):
        return "Yes" if obj.is_valid() else "No"

    is_valid_display.short_description = "Valid"

    def usage_display(self, obj):
        return f"{obj.usage_count} / {obj.usage_limit}"

    usage_display.short_description = "Usage"

    def download_url(self, obj):
        from django.urls import reverse, NoReverseMatch
        from django.utils.html import format_html

        try:
            url = reverse("filedrop:download", kwargs={"shortname": obj.drop.shortname})
            full_url = f"{url}?token={obj.token_value}"
            return format_html(
                '<a href="{}" target="_blank">{}</a>', full_url, full_url
            )
        except NoReverseMatch:
            return "URL not available"

    download_url.short_description = "Download URL"


@admin.register(DownloadLog)
class DownloadLogAdmin(admin.ModelAdmin):
    list_display = ["token", "ip_address", "timestamp", "success"]
    list_filter = ["success", "timestamp"]
    search_fields = ["token__drop__shortname", "ip_address"]
    readonly_fields = [
        "token",
        "ip_address",
        "user_agent",
        "timestamp",
        "success",
        "error_message",
    ]

    def has_add_permission(self, request):
        return False
