from rest_framework import viewsets

from kioskController.serializers import APIKeySerializer
from kioskController.models import APIkey


class APIKeyViewSet(viewsets.ModelViewSet):
    queryset = APIkey.objects.all()
    serializer_class = APIKeySerializer