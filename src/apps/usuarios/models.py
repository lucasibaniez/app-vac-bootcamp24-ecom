from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id} - {self.username}. {self.first_name} - {self.last_name}"