from django.test import TestCase
from articulos.models import Articulo, LONGITUD_MAXIMA
from django.core.exceptions import ValidationError

# Create your tests here.
class TestModels(TestCase):

    # se ejecuta antes de una prueba
    def setUp(self, nombre="pesas", cantidad=2, precio="899.90", descripcion="peas rusas de 200kg"):
        self.articulo = Articulo(
            nombre = nombre,
            cantidad = cantidad,
            precio = precio,
            descripcion = descripcion
        )
        return super().setUp()

    def test_return_object_articulo(self):   
        self.articulo.save() 
        self.assertEqual(self.articulo.nombre, str(self.articulo))

    def test_max_length_nombre(self):       
        self.articulo.nombre = "jkbskjbvskjbvsjksfjfkldjkljfkldsjfkladjkljakljfdk"
        self.assertLess(len(self.articulo.nombre), 100)

    # la prueba pasa porque el texto excede la longitud
    def test_longitud_excedida(self):
        self.articulo.nombre = "djkljakljfdkklkdsmklfmsklmfklsdmfklsdmfsdllklkjkljvkljkfljfkgkdljgdkljvklfdvflkdjvfdkljvkvkdljvkldfmvklmvklvklfdjvkfldvklvmlfkdvnfkdlvjfkdljfkdlmdmdskl"
        
        with self.assertRaises(ValidationError):
            self.articulo.full_clean()

    # def test_prueba_texto_error(self):
    #     self.articulo.nombre = "djkljakljfdkklkdsmklfmsklmfklsdmfklsdmfsdllklkjkljvkljkfljfkgkdljgdkljvklfdvflkdjvfdkljvkvkdljvkldfmvklmvklvklfdjvkfldvklvmlfkdvnfkdlvjfkdljfkdlmdmdskl"

    #     try:
    #         self.articulo.full_clean()
    #     except ValidationError as ex:
    #         msg = str(ex.message_dict['nombre'])
    #         print(msg)
    #         self.assertEquals(msg, LONGITUD_MAXIMA)

    def test_insercion_articulo(self):
        self.articulo.save()

        # probamos que se inserto el articulo
        self.assertEquals(Articulo.objects.all()[0], self.articulo)

    def test_insercion_articulo_nombre(self):
        self.articulo.save()
        articulo = Articulo.objects.first()

        # probamos que se guardo el nombre del articulo
        self.assertEquals(articulo.nombre, 'pesas')


        
