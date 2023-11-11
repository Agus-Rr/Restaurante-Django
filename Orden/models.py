from django.db import models
from Mesa.models import Mesa
from Plato.models import Plato

# Create your models here.

class Orden(models.Model):

    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    plato = models.ManyToManyField(Plato)

    estado = models.BooleanField(default=False)

    precioTotal = models.IntegerField()