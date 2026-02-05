from rest_framework import serializers

from kioskController.models import InfoMaterials


class InfoMaterialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoMaterials
        fields = '__all__'