from django.db import models

from apps.pacientes.models import Paciente
from apps.vacunas.models import Dosis
class VacunaAplicada(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dosis = models.ForeignKey(Dosis, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateField()
    # establecimiento medico 

    def __str__(self):
        return f"{self.paciente} - {self.dosis.vacuna} - {self.dosis}"