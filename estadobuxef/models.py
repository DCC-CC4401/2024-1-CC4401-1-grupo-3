from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UsuarioRegistrado(AbstractUser):
    pass

class Estudiante(UsuarioRegistrado):
    pass

class Reporte(models.Model):
    hora = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    lugar = models.ForeignKey('Lugar', on_delete=models.PROTECT)
    image = models.FileField(upload_to='uploads/estudiante/', blank=True, null=True)


class Lugar(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, default='Sin categoria')
    nombre = models.CharField('Nombre', max_length=50, null=False)
    data = models.JSONField(default=dict)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
