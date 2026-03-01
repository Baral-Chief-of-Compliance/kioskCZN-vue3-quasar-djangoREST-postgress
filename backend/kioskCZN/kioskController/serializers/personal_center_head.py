from rest_framework import serializers

from kioskController.models import PCHeadInfoPhone, PCHeadInfoEmail, PCHeadInfoTimeTable


class PCHeadInfoPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = PCHeadInfoPhone
        fields = '__all__'


class PCHeadInfoEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PCHeadInfoEmail
        fields = '__all__'


class PCHeadInfoTimeTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = PCHeadInfoTimeTable
        fields = '__all__'