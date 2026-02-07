from rest_framework import viewsets

from kioskController.models import Game
from kioskController.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all()
    serializer_class = GameSerializer