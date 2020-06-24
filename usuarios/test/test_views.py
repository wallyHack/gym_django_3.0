
from django.test import TestCase
from django.contrib.auth.models import User
from articulos.models import Articulo
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        return super().setUp()

    def test_redireccion_de_usuario_no_legeado(self):
        response = self.client.get('/usuarios/bienvenido/')
        self.assertRedirects(response, '/usuarios/login/')

    def test_url_login(self):
        response = self.client.get('/usuarios/login/')
        self.assertEquals(response.status_code, 200)

    def test_template_correcto_login(self):
        response = self.client.get('/usuarios/login/')
        self.assertTemplateUsed(response, 'usuarios/login.html')

    def test_url_registrar_usuario(self):
        response = self.client.get('/usuarios/registrar/')
        self.assertEquals(response.status_code, 200)

    def test_template_correcto_registrar_usuario(self):
        response = self.client.get('/usuarios/registrar/')
        self.assertTemplateUsed(response, 'usuarios/registrar.html')

    # def test_logear_usuario(self):
    #     # preparamos el ambiente de pruebas
    #     data = {
    #         'usuario': 'chino ',
    #         'contraseña': 'Manny001'
    #     }

    #     response = self.client.get('/usuarios/login/', data)
    #     print(User.objects.all())
