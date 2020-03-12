
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
    rfc = models.CharField('R.F.C', max_length=13)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    indice_masa = models.DecimalField(max_digits=3, decimal_places=2)

class Pago(models.Model):
    TIPO_PAGO = [
        ('1', 'Pago mensual'),
        ('2', 'Pago diario')   
    ]

    tipo_pago = models.CharField('Tipo de pago', max_length=1, choices=TIPO_PAGO)
    fecha = models.DateField('Fecha de pago', auto_now_add=True)
    cantidad = models.DecimalField(max_digits=7, decimal_places=2)
    usuario = models.ForeignKey(Usuario, verbose_name='Usuario', on_delete=models.SET_NULL, null=True)