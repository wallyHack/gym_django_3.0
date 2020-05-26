
from django.urls import path
from . import views

app_name = 'articulos'
urlpatterns = [
    path('hola/', views.hola, name="hola"),
    path('lista/', views.lista, name="lista_articulos"),
    path('<int:id_articulo>/eliminar/', views.eliminar, name='eliminar'),
    path('<int:id_articulo>/actualizar/', views.actualizar, name='actualizar'),
    path('agregar/', views.agregar, name='agregar'),
]
