from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django.contrib.auth import get_user_model

from django import forms

User = get_user_model()


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=64)
    username.label = "Username or Email"


class CustomUserCreationForm(UserCreationForm):
    display_name = forms.CharField(max_length=64, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'display_name']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'display_name')
