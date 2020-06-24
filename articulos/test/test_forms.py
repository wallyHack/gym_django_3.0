
from django.test import TestCase
from articulos.models import Articulo, LONGITUD_MAXIMA
from articulos.forms import ArticuloForm


class TestForms(TestCase):

    # se ejecuta antes de las pruebas
    def setUp(self, nombre="pesas", cantidad=2, precio="899.9", descripcion="pesas rusas de 200kg"):
        # datos del formulario
        self.data = {
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio,
            'descripcion': descripcion
        }

    def test_si_el_formulario_es_invalido(self):
        self.data['nombre'] = "djkljakljfdkklkdsmklfmsklmfklsdmfklsdmfsdllklkjkljvkljkfljfkgkdljgdkljvklfdvflkdjvfdkljvkvkdljvkldfmvklmvklvklfdjvkfldvklvmlfkdvnfkdlvjfkdljfkdlmdmdskl"
        form = ArticuloForm(
            self.data
        )
        # cuando la información va mal
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_es_valido(self):
        self.data['nombre'] = "banda elastica"
        self.data['cantidad'] = 80
        form = ArticuloForm(
            self.data
        )

        # cuando la información del form va bien
        return self.assertTrue(form.is_valid())

    def test_max_length_nombre(self):
        self.data['nombre'] = "djkljakljfdkklkdsmklfmsklmfklsdmfklsdmfsdllklkjkljvkljkfljfkgkdljgdkljvklfdvflkdjvfdkljvkvkdljvkldfmvklmvklvklfdjvkfldvklvmlfkdvnfkdlvjfkdljfkdlmdmdskl"
        form = ArticuloForm(
            self.data
        )

        return self.assertEquals(form.errors['nombre'], [LONGITUD_MAXIMA])

    # test con validadores personalizados
    def test_campo_stock_es_menor_a_30(self):
        self.data['cantidad'] = 3

        form = ArticuloForm(self.data)
        return self.assertEquals(form.errors['cantidad'], ['Error {0} es menor a 30'.format(self.data['cantidad'])])
