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
from .models import Evento
import calendar
from datetime import datetime
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

import calendar

def home_view(request) :
    mes = datetime.now().month
    context = {'mes': mes }
    return render(request, 'usuarios/home.html', context)

def documentos_view(request) :
     documentos = Documento.objects.all()
     context = {"documentos" : documentos}
     return render(request, 'usuarios/documentos.html', context)

from django.shortcuts import render
from .models import Solicitacao, Usuario

def notificacoes(request):
    matricula = request.user.username  # Ajuste para obter a matrícula do usuário logado
    try:

        # matricula = request.GET.get('matricula')
        usuario = Usuario.objects.get(matricula=matricula)
        solicitacoes = Solicitacao.objects.filter(aluno=usuario).order_by('-data_solicitacao')
    except Usuario.DoesNotExist:
        solicitacoes = []
    
    return render(request, 'usuarios/notificacoes.html', {'solicitacoes': solicitacoes})

def nova_solicitacao(request):
    form = SolicitacaoForm(request.POST or None)
    
    if form.is_valid():
        try:
            matricula = request.POST.get('matricula', '')
            usuario = Usuario.objects.get(matricula=matricula)
        except Usuario.DoesNotExist:
            messages.error(request, "Aluno não encontrado.")
            return redirect('nova_solicitacao')

        solicitacao = form.save(commit=False)
        solicitacao.aluno = usuario
        solicitacao.save()
        return redirect('notificacoes')
    else:
        form = SolicitacaoForm()
    return render(request, 'usuarios/nova_solicitacao.html', {'form': form})

from django.shortcuts import render
from django.utils import timezone
from .models import Evento
import calendar

def calendario_view(request, troca_mes):
    if request.method == 'POST' :

        if request.POST.get('troca_mes') == 'mes-posterior' :
            troca_mes = int(troca_mes)+1
            if troca_mes == 13 :
                troca_mes = 1

        elif request.POST.get('troca_mes') == 'mes-anterior' :
            troca_mes = int(troca_mes)-1
            if troca_mes == 0 :
                troca_mes = 12
        else:

            data = request.POST.get('data')
            descricao = request.POST.get('descricao')

            evento = Evento(
                data = data,
                descricao = descricao,
                tipo_servico = "texto",
                aluno = request.user
            )

            evento.save()

        return redirect('calendario', str(troca_mes))
    
    agora = datetime.now()
    ano = datetime.now().year
    mes = int(troca_mes)

    # Criar um calendário para o mês atual   
    cal = calendar.Calendar(firstweekday=0)
    dias = cal.monthdayscalendar(ano,mes)

    eventos = Evento.objects.all()
    for evento in eventos :
        data_evento = str(evento.data).split("-")
        evento.mes = int(data_evento[1])
        evento.dia = int(data_evento[2])

    return render(request, 'calendario.html', {
        'dias': dias,
        'mes_nome': calendar.month_name[mes],
        'ano': ano,
        'eventos': eventos,
        'troca_mes' : str(troca_mes),
        'mes' : mes,
    })
def nova_solicitacao_view(request):
    # Lógica para a página de nova solicitação
    return render(request, 'nova_solicitacao.html')