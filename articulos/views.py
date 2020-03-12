from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Articulo
from .forms import ArticuloForm

# Create your views here.

""" vistas basadas en funciones"""

def agregar(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos:lista_articulos')            
    else:
        form = ArticuloForm()
    
    return render(request, 'articulos/agregar_articulos.html', {'form': form})

def eliminar(request, id_articulo):
    articulo = get_object_or_404(Articulo, pk=id_articulo)
    articulo.delete()
    return redirect('articulos:lista_articulos')

def actualizar(request, id_articulo):
    instance = get_object_or_404(Articulo, pk=id_articulo)
    form = ArticuloForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('articulos:lista_articulos')

    return render(request, 'articulos/agregar_articulos.html', {'form': form})

def lista(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulos/lista_articulos.html', {'articulos': articulos})

def hola(request):
    context = {
        'nombre': 'Manuel',
        'apellido_p': 'Herrera',
        'edad': 19, 
        'estado': 'Zacatecas',
        'materias':  [
            'Arquitectura de SW',
            'Redes de Computadoras',
            'Testing',
            'Servicio Social'
        ]        
    }

    return render(request, 'articulos/index.html', context)


