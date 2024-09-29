from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de usuário', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

from .models import Solicitacao
from django.utils import timezone
import datetime
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")

    class Meta:
        model = Usuario
        fields = ['matricula', 'nome', 'idade', 'tipo_usuario']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha != confirmar_senha:
            raise ValidationError("As senhas não coincidem")

        return cleaned_data

