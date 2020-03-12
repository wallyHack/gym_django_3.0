
from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):

    class Meta:       
        fields = ('first_name','last_name',
        'email','rfc','fecha_nacimiento','peso',
        'altura','indice_masa',
        'username','password'
        )
        model = Usuario