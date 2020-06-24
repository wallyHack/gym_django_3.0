
from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
