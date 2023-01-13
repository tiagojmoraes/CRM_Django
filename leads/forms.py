from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, Agent

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    first_name=forms.CharField(
        label='Primeiro Nome',
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Inclua o seu Primeiro Nome'})
        )
    age=forms.CharField(
        min_length=1,
        max_length=3,
        label='Idade',
        widget=forms.TextInput(attrs={'placeholder':'Idade'})
        )

    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
            'description',
            'phone_number',
            'email',
        )

class LeadForm(forms.Form):
    first_name = forms.CharField(label='Seu Nome')
    last_name = forms.CharField(label='Segundo Nome')
    age = forms.IntegerField(min_value=0, max_value=100, label='Idade')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
        )
        field_classes = {"username": UsernameField}

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)        
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents

class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
