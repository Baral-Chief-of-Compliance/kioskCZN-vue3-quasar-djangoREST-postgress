from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from kioskController.models import Worker
from kioskController.serializers import WorkerSerializer



class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = [DjangoFilterBackend]