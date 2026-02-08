from rest_framework import viewsets
from rest_framework.decorators import action

from kioskController.serializers import DepartmentSerializer
from kioskController.models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer