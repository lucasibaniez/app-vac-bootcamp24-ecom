from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True)