from rest_framework import viewsets

from kioskController.models import Event
from kioskController.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer