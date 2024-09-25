from django.db import models

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    ]

    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    tipo_usuario = models.CharField(max_length=9, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.tipo_usuario})"

class Documento(models.Model) :
    documento = models.CharField(max_length=50)
    arquivo = models.ImageField(blank=True)

    def __str__(self) :
        return self.documento

from django.contrib.auth.models import User
from django.utils import timezone

class Solicitacao(models.Model):
    SERVICOS = [
        ('turma', 'Trocar de Turma'),
        ('matricula', 'Declaração de Matrícula'),
        ('irpf', 'Declaração de Imposto de Renda'),
    ]
    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_servico = models.CharField(max_length=20, choices=SERVICOS)
    motivo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    horario_funcionamento_inicio = models.TimeField(default="08:00")
    horario_funcionamento_fim = models.TimeField(default="18:00")

    def __str__(self):
        return f'{self.tipo_servico} - {self.aluno.username}'
