from django.shortcuts import render, redirect
from registro.forms import RegistroForm

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro')
    else:
        form = RegistroForm()
    
    return render(request, 'formulario.html', {'form': form})
    