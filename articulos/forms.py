
from django.forms import ModelForm
from .models import Articulo

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
