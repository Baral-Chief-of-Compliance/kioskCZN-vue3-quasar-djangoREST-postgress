from rest_framework import viewsets

from kioskController.models import Worker
from kioskController.serializers import WorkerSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer