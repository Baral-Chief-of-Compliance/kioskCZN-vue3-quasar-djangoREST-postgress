from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from kioskController.models import Room
from kioskController.serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]