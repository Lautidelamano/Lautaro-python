from audioop import add
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import formulario
from.models import Productos

# Create your views here.

def index(request):
    producto=Productos.objects.all()
    context = {'productos' : producto}
    return render(request, 'tienda/index.html', context)


def agregar(request):
    if request.method == 'POST':
        form = formulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = formulario()
    context ={'form':form}
    return render(request, 'tienda/agregar.html', context)


def eliminar(request, productos_id):
    productos = Productos.objects.get(id=productos_id)
    productos.delete()
    return redirect(index)