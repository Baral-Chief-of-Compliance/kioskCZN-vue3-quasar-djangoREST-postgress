from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from kioskController.models import Floor
from kioskController.serializers import FloorSerializer, FloorFullInfoSerializer


class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pc',]

    def get_serializer_class(self):
        if self.action == 'list':
            return FloorFullInfoSerializer
        else:
            return FloorSerializer