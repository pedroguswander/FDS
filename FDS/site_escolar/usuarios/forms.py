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
    class Meta:
        model = Solicitacao
        fields = ['tipo_servico', 'motivo', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        motivo = cleaned_data.get('motivo')
        descricao = cleaned_data.get('descricao')

        # Validação 1: Campos obrigatórios
        if not motivo or not descricao:
            raise forms.ValidationError("Todos os campos obrigatórios devem ser preenchidos.")

        # Validação 2: Verificar horário de funcionamento
        hora_atual = timezone.now().time()
        inicio_funcionamento = datetime.time(8, 0)  # 08:00
        fim_funcionamento = datetime.time(18, 0)  # 18:00

        if hora_atual < inicio_funcionamento or hora_atual > fim_funcionamento:
            raise forms.ValidationError("As solicitações só podem ser feitas entre 08:00 e 18:00.")