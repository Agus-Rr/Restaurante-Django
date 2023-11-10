from django.db import models

# Create your models here.

class Plato(models.Model):
    
    nombre = models.CharField(max_length=50)

    precio = models.IntegerField(max_length=10)


    def __str__(self):
        return self.nombre