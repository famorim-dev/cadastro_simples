from django.shortcuts import render, get_list_or_404
from registro.models import Registro

def listar_registro(request):
    registros = Registro.objects.all()
    contexto = {
        'registros': registros
    }
    return render(request, 'home.html', contexto)

def exibiruser(request, info_user):
    usuarios = get_list_or_404(Registro, id=info_user)
    exibir = {
        'usuarios': usuarios
    }
    return render(request, 'user.html', exibir)