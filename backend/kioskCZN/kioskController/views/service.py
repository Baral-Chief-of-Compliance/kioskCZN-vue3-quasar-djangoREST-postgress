from datetime import date
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from kioskController.models import Service, PC, Worker, WorkerInDepartment, Department
from kioskController.serializers import ServiceSerializer, WorkInDepartmentFullInfoSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('priority')
    serializer_class = ServiceSerializer

    def get_serializer_class(self):
        if self.action == 'get_service_worker_list':
            return WorkInDepartmentFullInfoSerializer
        else:
            return ServiceSerializer

    @action(detail=True, methods=['get'])
    def get_service_worker_list(self, request: Request, pk=None):
        """Получить всех работников конкретного центра занятости, 
        которые предоставляют услугу"""
        service = get_object_or_404(Service, pk=pk)

        pc_id = request.query_params.get('pc', None)

        if pc_id:
            pc_id = int(pc_id)
            pc = get_object_or_404(PC,pk=pc_id)
            deps = Department.objects.filter(pc=pc)

            worker_in_pc = WorkerInDepartment.objects\
            .filter(
                dep__in=deps
            )\
            .filter(visible=True)\
            .filter(date_get_info=date.today())\
            .filter(
                services=service
            )\
            .order_by('post__priority')

            serializer_class = self.get_serializer_class()
            serializer = serializer_class(worker_in_pc, many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                data={
                    'need send pc via query_param'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


