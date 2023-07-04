from django import forms
from .models import Speaker
from django.core.files.uploadedfile import InMemoryUploadedFile


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = '__all__'
