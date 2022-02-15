from audioop import add
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import formulario

# Create your views here.

lista=[]

def index(request):
    context = {'lista' : lista}
    return render(request, 'tienda/index.html', context)

def agregar(request):
    if request.method == 'POST':
        form = formulario(request.POST)
        if form.is_valid():
            listaAux=form.cleaned_data['Elemento']
            lista.append(listaAux)
            return redirect ('index')
    else:
        form = formulario()
    context ={'form':form}
    return render(request, 'tienda/agregar.html', context)
