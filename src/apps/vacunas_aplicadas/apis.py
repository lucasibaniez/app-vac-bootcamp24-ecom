from rest_framework import generics

from .models import VacunaAplicada
from .serializers import VacunacionSerializer

class VacunacionesCrearYListar(generics.ListCreateAPIView):
    queryset = VacunaAplicada.objects.all()
    serializer_class = VacunacionSerializer

