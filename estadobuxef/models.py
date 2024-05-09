from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UsuarioRegistrado(User):
    def __init__(self, *args, **kwargs):
        super(UsuarioRegistrado, self).__init__(*args, **kwargs)


class Estudiante(UsuarioRegistrado):
    def __init__(self, *args, **kwargs):
        super(Estudiante, self).__init__(*args, **kwargs)


class Reporte(models.Model):
    def __init__(self, *args, **kwargs):
        super(Reporte, self).__init__(*args, **kwargs)
        self.hora = models.DateTimeField(auto_now_add=True)
        self.contenido = models.TextField()
        self.lugar = models.ForeignKey('Lugar', on_delete=models.PROTECT)


class Lugar(models.Model):
    def __init__(self, *args, **kwargs):
        super(Lugar, self).__init__(*args, **kwargs)
        self.categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)


class Categoria(models.Model):
    def __init__(self, *args, **kwargs):
        super(Categoria, self).__init__(*args, **kwargs)
        self.nombre = models.CharField(max_length=50)
