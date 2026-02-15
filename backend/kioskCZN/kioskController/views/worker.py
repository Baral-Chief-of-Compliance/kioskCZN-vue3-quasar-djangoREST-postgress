from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from kioskController.models import Worker, Department, WorkerInDepartment
from kioskController.serializers import WorkerSerializer, WorkerInDepartmentSearch, WorkerInDepartmentSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    """Для работы с сотрудниками в системе"""
    queryset = Worker.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    serializer_class = WorkerSerializer


class WorkerInDepartmentViewSet(viewsets.ModelViewSet):
    """Работника в отделе"""
    queryset = WorkerInDepartment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    serializer_class = WorkerInDepartmentSerializer

    # def get_serializer_class(self):
    #     if self.action == 'find_by_fio_departments_pc':
    #         return WorkerInDepartmentSearch
    #     else:
    #         return WorkerInDepartmentSerializer


    # Метод по поиску работника в отеделе конкретного кц
    # @action(detail=False, methods=['post'])
    # def find_by_worker_id_department_name_pc(self)
    #     serializer_class = self.get_serializer_class()

    #     serializer_data = serializer_class(request.data)

    #     if serializer_data.is_valid():
    #         pc = get_object_or_404(MyModel, pk=serializer_data.validated_data['pc'])
    #         worker = get_object_or_404(Worker, pk=serializer_data.validated_data['worker_id'])
    #         dep = Department.objects.filter(
    #             pc=pc,
    #             name=serializer_data.validated_data['department_name']
    #         ).first()

    #         worker_in_department = WorkerInDepartment.objects.filter(
    #             worker=worker,
    #             dep=dep
    #         )

    #         if worker_in_department.count() == 0:
    #             return Response(
    #                 data={
    #                     'detail': 
    #                 }
    #             )

    #     else:
    #         return Response(
    #             serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )