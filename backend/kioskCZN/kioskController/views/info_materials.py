from rest_framework import viewsets

from kioskController.models import InfoMaterials
from kioskController.serializers import InfoMaterialsSerializer


class InfoMaterialsViewSet(viewsets.ModelViewSet):

    queryset = InfoMaterials.objects.all().order_by('priority')
    serializer_class = InfoMaterialsSerializer