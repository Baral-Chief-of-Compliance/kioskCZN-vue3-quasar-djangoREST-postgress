from rest_framework import serializers

from yandexApiKeys.models import YandexAPIKey


class YandexAPIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = YandexAPIKey
        fields = ('key',)