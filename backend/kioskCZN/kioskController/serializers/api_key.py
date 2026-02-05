from rest_framework import serializers

from kioskController.models import APIkey


class APIKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = APIkey
        fields = '__all__'