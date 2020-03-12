
from django.forms import ModelForm, TextInput, NumberInput
from .models import Articulo

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

        #personalizando elementos del formulario con estilos de bootstrap
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del articulo'}),
            'cantidad': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'precio': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),            
        }
