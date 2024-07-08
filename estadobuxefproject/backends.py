from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2SHA1PasswordHasher

class FuncionarioBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if username is None or password is None:
            return None
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None