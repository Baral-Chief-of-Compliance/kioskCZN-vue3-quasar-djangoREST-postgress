from rest_framework import viewsets

from kioskController.models import InfoMaterials
from kioskController.serializers import InfoMaterialsSerializer


class InfoMaterialsViewSet(viewsets.ModelViewSet):

    queryset = InfoMaterials.objects.all()
    serializer_class = InfoMaterialsSerializer