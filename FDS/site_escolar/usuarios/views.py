from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario
from .models import Documento
from .models import Solicitacao
from .forms import SolicitacaoForm
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')     
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro_view(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        tipo_usuario = request.POST.get('tipo_usuario')

        # Salvar os dados no banco de dados
        novo_usuario = Usuario(matricula=matricula, nome=nome, idade=idade, tipo_usuario=tipo_usuario)
        novo_usuario.save()

        return redirect('login')  # Redireciona para a página de login após o cadastro
    return render(request, 'usuarios/cadastro.html')

def home_view(request) :
    return render(request, 'usuarios/home.html')

def documentos_view(request) :
     documentos = Documento.objects.all()
     context = {"documentos" : documentos}
     return render(request, 'usuarios/documentos.html', context)

def notificacoes(request):
    solicitacoes = Solicitacao.objects.filter(aluno=request.user).order_by('-data_solicitacao')
    return render(request, 'usuarios/notificacoes.html', {'solicitacoes': solicitacoes})

def nova_solicitacao(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.aluno = request.user
            solicitacao.save()
            return redirect('notificacoes')
    else:
        form = SolicitacaoForm()
    
    return render(request, 'usuarios/nova_solicitacao.html', {'form': form})
