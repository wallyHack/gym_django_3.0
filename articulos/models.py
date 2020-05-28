from django.db import models
from django.core.validators import MaxLengthValidator
from articulos.validador import validate_cantidad

# Create your models here.
LONGITUD_MAXIMA = 'Error de longitud'

class Articulo(models.Model):
    nombre = models.CharField("Nombre", max_length=100, validators=[MaxLengthValidator(100)])
    cantidad = models.IntegerField("Stock", validators=[validate_cantidad])
    precio = models.DecimalField(
        "Precio unitario", max_digits=10, decimal_places=2)
    descripcion = models.TextField("Descripción", null=True, blank=True)

    def __str__(self):
        return self.nombre
