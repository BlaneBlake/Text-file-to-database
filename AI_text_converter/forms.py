from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserCreationForm

# from .models import
# from datetime import date
from django.core.exceptions import ValidationError


class TextToConvertForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Text to convert', required=False)
    file = forms.FileField(label='File to convert', required=False) # plik się nie ładuje, czemu????

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        file = cleaned_data.get("file")

        if not text and not file:
            raise ValueError('wypełnij jedno z pól')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('username', 'email')