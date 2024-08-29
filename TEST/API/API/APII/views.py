from rest_framework import viewsets
from app_1.models import Json
from API.APII.serializer import Jsonserializer
from django_filters.rest_framework import DjangoFilterBackend 

class Jsonviewset(viewsets.ModelViewSet):
    queryset = Json.objects.all()
    serializer_class = Jsonserializer
    filter_backends = [DjangoFilterBackend]  # Añadir el backend de filtros
    filterset_fields = ['id', 'devicename']   