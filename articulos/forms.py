
from django.forms import ModelForm, TextInput, NumberInput
from .models import Articulo, LONGITUD_MAXIMA

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

        # personalizando elementos del formulario con estilos de bootstrap
        widgets = {
            'nombre': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Nombre del articulo'
                }),
            'cantidad': NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Cantidad'
                }),
            'precio': NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Precio'
                }),
        }

        # mensajes personalizados para la validación backend
        error_messages = {
            'nombre': {'max_length': LONGITUD_MAXIMA}
        }
