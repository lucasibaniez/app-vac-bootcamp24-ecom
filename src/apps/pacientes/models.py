from django.db import models

from apps.vacunas.models import Dosis

GENERO_MASCULINO = "M"
GENERO_FEMENINO = "F"
GENERO_NO_BINARIO = "X"

GENERO_CHOICES = (
    (GENERO_MASCULINO, "Masculino"), 
    (GENERO_FEMENINO, "Femenino"), 
    (GENERO_NO_BINARIO, "No binario")
)


class Paciente(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    genero = models.CharField(choices=GENERO_CHOICES)

    # dosis = models.ManyToManyField(Dosis)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"