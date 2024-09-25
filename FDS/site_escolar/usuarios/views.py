from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario
from .models import Documento
from .models import Solicitacao
from .forms import SolicitacaoForm
from django.contrib import messages
from .forms import CadastroForm
from django.contrib.auth.hashers import make_password

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

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CadastroForm
from django.contrib import messages

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            matricula = form.cleaned_data['matricula']
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            tipo_usuario = form.cleaned_data['tipo_usuario']
            senha = form.cleaned_data['senha']
            confirmar_senha = form.cleaned_data['confirmar_senha']

            if senha == confirmar_senha:
                # Cria o usuário no modelo User do Django
                usuario = User.objects.create(
                    username=matricula,
                    first_name=nome,
                    password=make_password(senha)
                )

                # Salva o tipo de usuário e outros dados no modelo Usuario
                Usuario.objects.create(
                    matricula=matricula,
                    nome=nome,
                    idade=idade,
                    tipo_usuario=tipo_usuario
                )

                return redirect('login')  # Redireciona para a página de login após o cadastro
            else:
                form.add_error('confirmar_senha', 'As senhas não coincidem.')
    else:
        form = CadastroForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})

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
