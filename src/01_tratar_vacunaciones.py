import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.vacunas_aplicadas.models import VacunaAplicada

archivo = open("vacunaciones.txt", "w")

archivo.write(f"apellido y nombre; fecha; nombre vacuna; dosis\n")
for vac in VacunaAplicada.objects.all():
    archivo.write(f"{vac.paciente}; {vac.fecha_aplicacion}; {vac.dosis.vacuna}; {vac.dosis.nombre}\n")
    print("-->vac", vac)
    
archivo.close()