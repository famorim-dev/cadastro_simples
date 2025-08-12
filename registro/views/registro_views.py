from django.shortcuts import render, get_list_or_404
from registro.models import Registro

# Exibe a lista de registros ordenada pelo ID em ordem decrescente
def listar_registro(request):
    registros = Registro.objects.all()
    registros = Registro.objects.order_by('-id')
    contexto = {
        'registros': registros
    }
    return render(request, 'home.html', contexto)

# Pesquisa registros pelo campo 'nome' (case insensitive) e exibe resultados
def pesquisa(request):
    query = request.GET.get('q', '').strip()

    if query:
        pesquisas = Registro.objects.filter(nome__icontains=query)
    else:
        pesquisas = Registro.objects.all()

    return render(request, 'home.html', {'registros': pesquisas, 'query': query})

# Exibe os detalhes de um usuário específico baseado no ID (info_user)
def exibiruser(request, info_user):
    usuarios = get_list_or_404(Registro, id=info_user)
    exibir = {
        'usuarios': usuarios
    }
    return render(request, 'user.html', exibir)