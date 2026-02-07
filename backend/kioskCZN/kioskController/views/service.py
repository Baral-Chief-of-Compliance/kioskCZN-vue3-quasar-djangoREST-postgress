from rest_framework import viewsets

from kioskController.models import Service
from kioskController.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer