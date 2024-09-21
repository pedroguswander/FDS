from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario


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