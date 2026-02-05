from rest_framework import viewsets

from kioskController.models import Floor
from kioskController.serializers import FloorSerializer


class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer