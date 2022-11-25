from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(
        max_length='15', min_length='5', label='Usuario')
    first_name = forms.CharField(
        max_length='15', min_length='5', label='Nombre')
    last_name = forms.CharField(
        max_length='15', min_length='5', label='Apellido')
    email = forms.EmailField(
        label='e-mail')
    password1 = forms.CharField(
        widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(
        widget=forms.PasswordInput, label='Confirmar contraseña')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]