from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Personaje(models.Model):
    """
    Describe un personaje.
    """
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField(null=True)
    imagen = models.CharField(max_length=1000, verbose_name='Imágen', help_text='URL de la imagen del personaje', blank=True)

    def __str__(self):
        return self.nombre

class Deseo(models.Model):
    """
    Describe a un deseo.
    """
    deseo = models.CharField(max_length=400)
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)

    def __str__(self):
        return self.deseo