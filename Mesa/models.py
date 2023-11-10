from django.db import models

# Create your models here.

class Mesa(models.Model):

    cantCubiertos = models.IntegerField()

    disponible = models.BooleanField(default=False)
    #ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
