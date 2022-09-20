from django import forms
from .models import URL


class CreateLink(forms.ModelForm):
    link_full = forms.URLField(label="Link")

    class Meta:
        model = URL
        fields = ('link_full',)
