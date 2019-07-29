from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MyUser
from wallet.settings import GENERO_CHOICES
from django.conf import settings
from wallet.settings import BASE_DIR


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nome'
            }
        )
    )
    last_name = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Sobrenome'
            }
        )
    )
    email = forms.EmailField(label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Email'
            }
        )
    )

    password1 = forms.CharField(label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Senha'
            }
        )
    )

    password2 = forms.CharField(label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Confirmar senha'
            }
        )
    )

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class InfoForm(forms.ModelForm):
    email = forms.EmailField(
        label='Informe seu email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira aqui seu email'
            }
        )
    )

    first_name = forms.CharField(
        label='Informe seu primeiro nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Informe aqui seu primeiro nome'
            }
        )
    )

    last_name = forms.CharField(
        label='Informe seu ultimo nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Informe aqui seu ultimo nome'
            }
        )
    )

    nascimento = forms.DateField(
        label='Informe sua data de nascimento',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    genero = forms.Select(
        choices=GENERO_CHOICES,
    )

    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name', 'nascimento', 'genero']