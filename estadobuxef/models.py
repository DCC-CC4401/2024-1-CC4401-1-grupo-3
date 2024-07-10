from django.contrib.auth.models import User, Permission, AbstractUser, AbstractBaseUser
from django.db import models
from django.db.models import TextField, EmailField

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

class Funcionario(AbstractBaseUser): 
    username = TextField(max_length=50, blank=False)
    email = EmailField(null=False, unique=True)
    class Meta:
        permissions = [("can_change_status", "Can change the status of a report")]
    

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
    STATE_CHOICES = (
        ('A', 'Aprobado'),
        ('R', 'Rechazado'),
        ('P', 'Pendiente'),
    )
    usuario = models.ForeignKey(Estudiante, null=True, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    lugar = models.ForeignKey('Lugar', on_delete=models.PROTECT)
    image = models.FileField(upload_to='uploads/estudiante/', blank=True, null=True)
    estado = models.CharField(max_length=1, choices=STATE_CHOICES, default='P', null= True)  # default='P' is a good practice to avoid null


class Lugar(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, default='Sin categoria')
    nombre = models.CharField('Nombre', max_length=50, null=False)
    data = models.JSONField(default=dict)
    #imagen = models.FileField(upload_to='uploads/lugar/', blank=True, null=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)