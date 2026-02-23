from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from kioskController.models import PC, Department
from kioskController.serializers import PCSerializer


class PCViewSet(viewsets.ModelViewSet):

    queryset = PC.objects.all()
    serializer_class = PCSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    @action(detail=True, methods=['get'])
    def get_departments(self, request, pk=None):
        pc = get_object_or_404(PC, pk=pk)

        #Получаем все отделы, котрые видно
        deps = Department.objects.filter(
            pc=pc,
            visible=True
        ).order_by('priority')

        