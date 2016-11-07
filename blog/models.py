from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Computadora(models.Model):
    autor = models.ForeignKey('auth.User')
    precio = models.FloatField();
    descripcion = models.TextField();
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE,)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.categoria



# Create your models here.
