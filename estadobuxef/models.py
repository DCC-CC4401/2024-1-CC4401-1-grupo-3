from django import forms
from django.contrib.auth.models import User
from django.db import models

"""
** Models **
``UsuarioRegistrado``
    A model that inherits from the Django User model to use
    as base for the Estudiante model.
    
``Estudiante``
    A model that inherits from the UsuarioRegistrado model 
    that represents a student user. In the future, this model
    will have different behavoir than other registered users.
"""


class UsuarioRegistrado(User):
    pass


class Estudiante(UsuarioRegistrado):
    pass


"""
** Models **
``Reporte``
    A model that represents a report of an event. It has a
    date, a content, a place and an optional image.
    
``Lugar``
    A model that represents a place. It has a reference to a category,
    a name and a data field that can store any JSON data.
    
``Categoria``
    A model that represents a category for a place.
"""


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


"""
** Models **
``NuevoReporteForm``
    A form that inherits from the Django ModelForm to create
    a new report.
"""


class NuevoReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['contenido', 'lugar']
