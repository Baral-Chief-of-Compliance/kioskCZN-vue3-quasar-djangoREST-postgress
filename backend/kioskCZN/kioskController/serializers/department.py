from datetime import datetime

from rest_framework import serializers


from kioskController.models import Department, Worker, WorkerInDepartment
from kioskController.serializers.worker import WorkInDepartmentFullInfoSerializer


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentWithModifiedNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='modified_name')  # используем аннотированное поле

    workers = serializers.SerializerMethodField('get_workers')

    def get_workers(self, obj: Department):
        """Получить работников отдела"""
        today = datetime.today()

        worker = WorkerInDepartment.objects.filter(
            dep=obj,
            visible=True,
            date_get_info=today.date()
        ).order_by('-head_of_dep', 'post')

        serializer = WorkInDepartmentFullInfoSerializer(worker, many=True)

        return serializer.data

    
    class Meta:
        model = Department
        fields = ['id', 'name', 'priority', 'visible', 'pc', 'workers']