from django import forms
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
    hora = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    lugar = models.ForeignKey('Lugar', on_delete=models.PROTECT)
    image = models.FileField(upload_to='uploads/estudiante/', blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super(Reporte, self).__init__(*args, **kwargs)


class Lugar(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, default='Sin categoria')
    def __init__(self, *args, **kwargs):
        super(Lugar, self).__init__(*args, **kwargs)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, db_default='Sin categoría')
    def __init__(self, *args, **kwargs):
        super(Categoria, self).__init__(*args, **kwargs)


class NuevoReporteForm(forms.ModelForm):

    class Meta:
        model = Reporte
        fields = ['contenido', 'lugar']
