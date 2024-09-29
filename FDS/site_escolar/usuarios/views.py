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
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
    return render(request, 'usuarios/login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CadastroForm
from django.contrib import messages

def cadastro_view(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        tipo_usuario = request.POST.get('tipo_usuario')
        curso = request.POST.get('curso')
        endereco = request.POST.get('endereco')
        periodo_ingresso = request.POST.get('periodo_ingresso')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

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
                    tipo_usuario=tipo_usuario,
                    curso=curso,
                    endereco = endereco,
                    periodo_ingresso = periodo_ingresso,
                    usuario= usuario,
                )

                return redirect('login')

    return render(request, 'usuarios/cadastro.html')

    
import calendar

def home_view(request) :
    mes = datetime.now().month
    ano =  datetime.now().year
    context = {'mes': mes, 'ano': ano }
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

def calendario_view(request, troca_mes, troca_ano):
    if request.method == 'POST' :

        if request.POST.get('troca_mes') == 'mes-posterior' :
            troca_mes = int(troca_mes)+1
            if troca_mes == 13 :
                troca_ano = int(troca_ano)+1
                troca_mes = 1

        elif request.POST.get('troca_mes') == 'mes-anterior' :
            troca_mes = int(troca_mes)-1
            if troca_mes == 0 :
                troca_ano = int(troca_ano)-1
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

        return redirect('calendario', str(troca_mes), str(troca_ano))
    
    agora = datetime.now()
    ano = int(troca_ano)
    mes = int(troca_mes)

    # Criar um calendário para o mês atual   
    cal = calendar.Calendar(firstweekday=0)
    dias = cal.monthdayscalendar(ano,mes)

    eventos = Evento.objects.filter(aluno = request.user)
    for evento in eventos :
        data_evento = str(evento.data).split("-")
        evento.mes = int(data_evento[1])
        evento.dia = int(data_evento[2])
        evento.ano = int(data_evento[0])

    return render(request, 'calendario.html', {
        'dias': dias,
        'mes_nome': calendar.month_name[mes],
        'eventos': eventos,
        'troca_mes' : str(troca_mes),
        'troca_ano' : str(troca_ano),
        'mes' : mes,
        'ano': ano,
    })
def nova_solicitacao_view(request):
    # Lógica para a página de nova solicitação
    return render(request, 'nova_solicitacao.html')

def usuario_view(request) :
    pessoa = Usuario.objects.get(usuario= request.user)
    context = {"usuario" : pessoa}

    return render(request, 'usuarios/usuario.html', context)