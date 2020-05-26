
from django.urls import path
from .views import Nuevo

app_name = 'usuarios_uaz'
urlpatterns = [
    path('nuevo/', Nuevo.as_view(), name='nuevo'),
]
