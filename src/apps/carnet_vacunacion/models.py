from django.db import models

from apps.pacientes.models import Paciente

class CarnetVacunacion(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    # fecha_creacion 
