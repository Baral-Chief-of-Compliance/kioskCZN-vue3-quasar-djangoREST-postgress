from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from kioskController.models import GameUrl
from kioskController.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):

    queryset = GameUrl.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pc',]