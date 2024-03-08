from django.forms import ModelForm
from .models import Comida, Bebida, Snack

class ComidaForm(ModelForm):
    class Meta:
        model = Comida
        fields = [
            'nombre',
            'origen',
            'calorias',
            'ingredientes'
        ]
    
class BebidaForm(ModelForm):
    class Meta:
        model = Bebida
        fields = [
            'nombre',
            'sabor',
            'marca',
            'calorias'
        ]

class SnackForm(ModelForm):
    class Meta:
        model = Snack
        fields = [
            'nombre',
            'calorias',
            'ingredientes'
        ]