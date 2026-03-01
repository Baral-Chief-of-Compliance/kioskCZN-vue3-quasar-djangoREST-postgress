from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from kioskController.models import Event
from kioskController.serializers import EventSerializer



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pc',]