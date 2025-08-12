from django.shortcuts import render, redirect, get_object_or_404
from registro.forms import RegistroForm
from registro.forms import CreateUser
from registro.forms import EditUserForm
from registro.models import Registro
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            novo_registro = form.save(commit=False)
            novo_registro.owner = request.user
            novo_registro.save()
            return redirect('registro')
    else:
        form = RegistroForm()
    
    return render(request, 'formulario.html', {'form': form})


def editarUsuario(request, id):
    usuario = get_object_or_404(Registro, pk=id, owner=request.user)

    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('registro')
    else:
        form = RegistroForm(instance=usuario)
    
    return render(request, 'formulario.html', {'form': form})

def deletarUsuario(request, id):
    usuario = get_object_or_404(Registro, pk=id, owner=request.user)

    if request.method == 'POST':
        usuario.delete()
        return redirect('registro')
    
    return render(request, 'deletar.html', {'usuario': usuario})


#formulario de logins CRIAR, ENTRAR, EDITAR

def criarUser(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'criar.html', {'form': form})

def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('registro')
        else:
            messages.error(request, 'Login inválido')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def editarPerfil(request):
    user = request.user
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('editarPerfil')
    else:
        form = EditUserForm(instance=user)

    return render(request, 'editar_perfil.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')