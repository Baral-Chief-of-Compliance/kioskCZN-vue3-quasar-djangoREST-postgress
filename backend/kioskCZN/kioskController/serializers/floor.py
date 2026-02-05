from rest_framework import serializers

from kioskController.models import Floor


class FloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = '__all__'