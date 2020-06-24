
from django.test import TestCase
from django.contrib.auth.models import User
from articulos.models import Articulo
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        return super().setUp()

    def test_url_lista_articulos(self):
        # # se logea el usuario en caso de ser requerido
        # User.objects.create_user(username="manuel", password="wally98")
        # # se lanza la ventana de login
        # self.client.login(username="manuel", password="wally98")

        response = self.client.get('/articulos/lista/')
        self.assertEquals(response.status_code, 200)

    def test_template_correcto_lista_articulos(self):
        response = self.client.get('/articulos/lista/')
        self.assertTemplateUsed(response, 'articulos/lista_articulos.html')

    def test_url_agregar_articulo(self):
        response = self.client.get('/articulos/agregar/')
        self.assertEquals(response.status_code, 200)

    def test_template_correcto_agregar_articulos(self):
        response = self.client.get("/articulos/agregar/")
        self.assertTemplateUsed(response, 'articulos/agregar_articulos.html')

    # me falta incluir pruebas de redireccion

    def test_agregar_articulo_form(self):
        # datos del form
        data = {
            'nombre': 'cuerdas elasticas',
            'cantidad': 67,
            'precio': 178.89,
            'descripcion': 'cuerdas para ejercer la masa muscular'
        }

        # envio los datos por post
        self.client.post('/articulos/agregar/', data)
        self.assertEquals(Articulo.objects.count(), 1)

    def test_template_correcto_index_articulos(self):
        response = self.client.get('/articulos/hola/')
        self.assertTemplateUsed(response, 'articulos/index.html')

    def test_eliminacion_correcta_de_articulo_existente(self):
        # preparamos el ambiente
        # primero creamos el articulo y lo guardamos en la DB
        Articulo.objects.create(
            nombre='cuerdas elasticas',
            cantidad=67,
            precio=178.89,
            descripcion='cuerdas para ejercer la masa muscular'
        )
        id = Articulo.objects.first().id  # obtenemos su ID
        # print(id)
        # print(Articulo.objects.count())

        # ahora lo eliminamos
        response = self.client.get('/articulos/'+str(id)+'/eliminar/')
        # print(response)
        self.assertEquals(response.url, '/articulos/lista/')
        self.assertEquals(Articulo.objects.count(), 0)
        # self.assertEquals(response.status_code, 301)
        # self.assertRedirects(response, '/articulos/lista_articulos.html')

    def test_eliminacion_articulo_no_existente(self):
        response = self.client.get('/articulos/10880/eliminar/')
        self.assertEquals(response.status_code, 404)

    def test_actualizacion_correcta_de_un_articulo(self):
        # lo creamos y guardamos en la DB
        Articulo.objects.create(
            nombre='cuerdas elasticas',
            cantidad=67,
            precio=178.89,
            descripcion='cuerdas para ejercer la masa muscular'
        )

        # obtenemos su ID
        id = Articulo.objects.first().id

        # hacemos la actualizacion
        # datos actualizados del form
        data = {
            'nombre': 'cuerdas elasticas de UAZ',
            'cantidad': 6798,
            'precio': 178.89,
            'descripcion': 'cuerdas para ejercer la masa muscular'
        }
        response = self.client.post('/articulos/'+str(id)+'/actualizar/', data)
        self.assertEquals(response.url, '/articulos/lista/')

    def test_actualizacion_de_articulo_no_existente(self):
        response = self.client.get('/articulos/2390/actualizar/')
        self.assertEquals(response.status_code, 404)
