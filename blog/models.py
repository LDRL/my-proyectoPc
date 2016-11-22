from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    activo = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre=models.CharField(max_length=100)
    activo = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.nombre

class Computadora(models.Model):
    autor = models.ForeignKey('auth.User')
    precio = models.FloatField();
    descripcion = models.TextField();
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,)
    imagen = models.ImageField(null=True, blank=True,upload_to='blog/fotos')
    activo = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.descripcion

    def photo_delete(sender, instance, **kwargs):
    #""Borra los ficheros de las fotos que se eliminan""
        instance.imagen.delete(false)


        #print vars()["a%s" % b]



# Create your models here.
