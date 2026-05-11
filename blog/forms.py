from django import forms


class ContactMessageForm(forms.Form):
    name = forms.CharField(max_length=120)
    social_url = forms.URLField(max_length=300, required=False)
    company = forms.CharField(max_length=160, required=False)
    email = forms.EmailField(max_length=254)
    brief = forms.CharField(max_length=4000, widget=forms.Textarea)
