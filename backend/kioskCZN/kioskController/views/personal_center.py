from rest_framework import viewsets

from kioskController.models import PC
from kioskController.serializers import PCSerializer


class PCViewSet(viewsets.ModelViewSet):

    queryset = PC.objects.all()
    serializer_class = PCSerializer