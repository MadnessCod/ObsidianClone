from django import forms
from django.core.exceptions import ValidationError

from .models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["file"]

    def clean_file(self):
        file = self.cleaned_data["file"]
        if not file.name.endswith('.md'):
            raise ValidationError("File must have .md extension")
        return file


class TextFrom(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
