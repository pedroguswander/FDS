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

