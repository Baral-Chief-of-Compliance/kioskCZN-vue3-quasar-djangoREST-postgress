from rest_framework import serializers

from kioskController.models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        models = Department
        fields = '__all__'