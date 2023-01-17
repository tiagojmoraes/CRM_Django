from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class CustomAuthenticationForm (AuthenticationForm):
    username = UsernameField(
        label="Username or E-mail",
        widget=forms.TextInput(attrs={'placeholder': 'Insert your E-mail or Username here.'})
    )

    password = UsernameField(
        # widget=forms.TextInput(attrs={'placeholder': 'Insert your password here.'})
        widget=forms.PasswordInput(attrs={'placeholder': 'Insert your password here.'})
    )