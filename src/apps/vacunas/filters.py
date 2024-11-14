import django_filters

from .models import Vacuna

class VacunaFiltro(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Vacuna
        fields = ['nombre', 'ca_dosis']