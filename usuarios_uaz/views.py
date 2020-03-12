from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UsuarioForm
from .models import Usuario
from django.urls import reverse_lazy

# Create your views here.
class Nuevo(CreateView):
    form_class = UsuarioForm
    model = Usuario
    template_name = 'usuarios_uaz/nuevo.html'
    success_url = reverse_lazy('usuarios_uaz:nuevo')