from rest_framework import serializers

from kioskController.models import Worker, WorkerInDepartment


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'


class WorkerInDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerInDepartment
        fields = '__all__'


class WorkerInDepartmentSearch(serializers.Serializer):
    """Сериализатор для поиска сотрудников"""
    worker_id = serializers.IntegerField(min_value=1)
    pc = serializers.IntegerField(min_value=1)
    department_name = serializers.CharField(max_length=256)