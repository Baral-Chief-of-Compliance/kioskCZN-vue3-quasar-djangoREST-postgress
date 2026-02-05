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