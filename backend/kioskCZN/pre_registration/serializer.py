from rest_framework import serializers

from pre_registration.models import PreRegistration, PreRegistrationRecord


class PreRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор пререгистрации"""

    class Meta:
        model = PreRegistration
        fields = '__all__'


class PreRegistrationRecordSerializer(serializers.ModelSerializer):
    """Сериализатор кода пререгистарции"""

    class Meta:
        model = PreRegistrationRecord
        fields = '__all__'