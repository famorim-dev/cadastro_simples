from django.shortcuts import render, redirect, get_object_or_404
from registro.forms import RegistroForm
from registro.models import Registro


def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro')
    else:
        form = RegistroForm()
    
    return render(request, 'formulario.html', {'form': form})


def editarUsuario(request, id):
    usuario = get_object_or_404(Registro, pk=id)

    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('registro')
    else:
        form = RegistroForm(instance=usuario)
    
    return render(request, 'formulario.html', {'form': form})

def deletarUsuario(request, id):
    usuario = get_object_or_404(Registro, pk=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('registro')
    
    return render(request, 'deletar.html', {'usuario': usuario})