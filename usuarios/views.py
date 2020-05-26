from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.


def hola(request):
    return render(request, 'usuarios/hola.html', {})


def bienvenido(request):
    if not request.user.is_authenticated:
        return redirect('usuarios:login')
    else:
        return render(request, 'usuarios/bienvenido.html', {})


def registrar(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(request.POST or None)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('usuarios:bienvenido')

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuarios/registrar.html", {'form': form})


def login_view(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('usuarios:bienvenido')

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuarios/login.html", {'form': form})


def logout_view(request):
    # finalizamos la sesión
    logout(request)
    # redireccionamos a la página de inicio(O de éxito)
    return redirect('usuarios:login')
