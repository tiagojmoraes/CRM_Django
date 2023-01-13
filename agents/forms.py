from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class AgentModelForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Seu Nome',
        widget=forms.TextInput(attrs={'placeholder':'Digite o seu Primeiro Nome'})
        )
    last_name = forms.CharField(
        label='Segundo Nome',
        widget=forms.TextInput(attrs={'placeholder':'Digite o seu Segundo Nome'})
        )
    email = forms.CharField(
        min_length=5,
        max_length=50,
        label='E-Mail',
        widget=forms.TextInput(attrs={'placeholder':'Inclua o seu principal e-mail'})
        )

    class Meta:
        model = User
        fields = (
            # 'username',
            'first_name',
            'last_name',
            'email',
        )