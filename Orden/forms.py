from django.db.models.base import Model
from django.forms import ModelForm
from .models import Orden
from Plato.models import Plato
from Mesa.models import Mesa

class ordenForm(ModelForm):
    class Meta:
        model = Orden
        fields = ['mesa','plato']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mesa'].queryset = Mesa.objects.filter(disponible = True) 


