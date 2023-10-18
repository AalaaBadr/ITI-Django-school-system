from django import forms
from .models import *


class AddTrack(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['name']
