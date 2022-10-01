from django import forms
from .models import URL
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateLink(forms.ModelForm):
    link_full = forms.URLField(label="Link")

    class Meta:
        model = URL
        fields = ('link_full',)

class MyRegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(
        label='Password confirm',
        widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
