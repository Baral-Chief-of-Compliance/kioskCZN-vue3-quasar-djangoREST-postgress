from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db.models import Q, Case, When, Value, CharField, F
from django.db.models.functions import Concat
from rest_framework.response import Response
from rest_framework import status

from kioskController.models import PC, Department, ShowDepartmentInOtherPC
from kioskController.serializers import PCSerializer, PCDetailSerializer, DepartmentWithModifiedNameSerializer


class PCViewSet(viewsets.ModelViewSet):

    queryset = PC.objects.all()
    serializer_class = PCSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PCDetailSerializer
        elif self.action == "get_departments":
            return DepartmentWithModifiedNameSerializer
        else:
            return PCSerializer

    @action(detail=True, methods=['get'])
    def get_departments(self, request, pk=None):
        """Получим отделы, которые видно и их сотрудников"""
        pc = get_object_or_404(PC, pk=pk)

        #Получаем отделы, которые отображаются в данном кц
        other_deps_ids = ShowDepartmentInOtherPC.objects.filter(
            pc=pc,
        ).values_list('dep_id', flat=True)

        # Объединяем условия через Q объекты
        all_deps = Department.objects.filter(
            Q(pc=pc, visible=True) | Q(id__in=other_deps_ids, visible=True)
        ).annotate(
            modified_name=Case(
                When(id__in=other_deps_ids, 
                    then=Concat(F('pc__name'), Value(' КЦ '), F('name'), output_field=CharField())),
                default=F('name'),
                output_field=CharField()
            )
        ).order_by('priority').distinct()


        serializer_class = self.get_serializer_class()
        serializer = serializer_class(all_deps, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )



        