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

class SolicitacaoForm(forms.ModelForm):
    matricula = forms.CharField(max_length=20, required=True)
    class Meta:
        model = Solicitacao
        fields = [ 'tipo_servico', 'motivo', 'descricao']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
            'tipo_servico': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        motivo = cleaned_data.get('motivo')
        descricao = cleaned_data.get('descricao')

        # Validação 1: Campos obrigatórios
        if not motivo or not descricao:
            raise forms.ValidationError("Todos os campos obrigatórios devem ser preenchidos.")
