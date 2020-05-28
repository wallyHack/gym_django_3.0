
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# validador personalizado para el campo nombre
def validate_cantidad(value):
    if value <= 30:
        raise ValidationError(
            _('Error {0} es menor a 30'.format(value)),            
        )