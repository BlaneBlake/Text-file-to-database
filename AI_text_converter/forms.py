from django import forms
from django.contrib.auth.forms import UserCreationForm

# from .models import
from datetime import date
from django.core.exceptions import ValidationError

class TextToConvertForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Text to convert')