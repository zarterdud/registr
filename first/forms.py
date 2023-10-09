from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(
            attrs={"class": "form-input"})
    )

    class Meta:
        model = User
        fields = ("username", "password1")
