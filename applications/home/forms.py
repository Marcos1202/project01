from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        #perzonalizar form
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'ingrese el texto aqui'
                }
            )
        }

    #funcion para validar un campo
    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 10 :
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad
        