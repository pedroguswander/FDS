from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de usuário', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

from .models import Solicitacao
from django.utils import timezone
import datetime

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