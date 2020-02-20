from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    cantidad = models.IntegerField("Stock")
    precio = models.DecimalField("Precio unitario", max_digits=10, decimal_places=2)
    descripcion = models.TextField("Descripción", null=True, blank=True)

    def __str__(self):
        return self.nombre