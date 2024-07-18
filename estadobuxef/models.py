from django.contrib.auth.models import User, Permission, AbstractUser, AbstractBaseUser, PermissionsMixin, \
    BaseUserManager, Group
from django.db import models
from django.db.models import TextField, EmailField

from estadobuxefproject import settings

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


class Estudiante(models.Model):
    foto = models.ImageField(upload_to='uploads/estudiante/', blank=True, null=False, default='static/images/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    favoritos = models.ManyToManyField('Lugar', blank=True)


class FuncionarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        user = self.model(email=email, username=username, **extra_fields)
        email = self.normalize_email(email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


# class Funcionario(AbstractBaseUser, PermissionsMixin):
#     class Meta:
#         permissions = [("can_change_status", "Can change status of reports")]
#
#     username = TextField(max_length=50, blank=False)
#     email = EmailField(null=False, unique=True)
#
#     groups = models.ManyToManyField(Group, related_name='funcionario_set', blank=True,
#         help_text='The groups this user belongs to.', verbose_name='groups', )
#     user_permissions = models.ManyToManyField(Permission, related_name='funcionario_permissions_set', blank=True,
#         help_text='Specific permissions for this user.', verbose_name='user permissions', )
#
#     objects = FuncionarioManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

class Funcionario(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

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
    STATE_CHOICES = (('A', 'Aprobado'), ('R', 'Rechazado'), ('P', 'Pendiente'),)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    lugar = models.ForeignKey('Lugar', on_delete=models.PROTECT)
    foto = models.FileField(upload_to='uploads/estudiante/', blank=True, null=True)
    estado = models.CharField(max_length=1, choices=STATE_CHOICES, default='P',
                              null=True)  # default='P' is a good practice to avoid null


class Lugar(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, default='Sin categoria')
    nombre = models.CharField('Nombre', max_length=50, null=False)
    data = models.JSONField(
        default=dict)  # imagen = models.FileField(upload_to='uploads/lugar/', blank=True, null=True)
    foto = models.ImageField(upload_to='uploads/lugar/', blank=True, null=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    foto = models.ImageField(upload_to='uploads/categoria/', null=True)