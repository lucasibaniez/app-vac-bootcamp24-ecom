from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    es_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.username}. {self.first_name} - {self.last_name}"