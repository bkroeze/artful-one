from django import forms


class TokenGenerationForm(forms.Form):
    """Form for generating new tokens."""

    expiration_days = forms.IntegerField(
        min_value=1,
        max_value=365,
        initial=30,
        label="Expires in (days)",
        help_text="Number of days until token expires",
    )
    usage_limit = forms.IntegerField(
        min_value=1,
        max_value=1000,
        initial=10,
        label="Usage limit",
        help_text="Maximum number of downloads allowed",
    )
