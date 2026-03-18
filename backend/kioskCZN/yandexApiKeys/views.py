from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from yandexApiKeys.models import YandexAPIKey
from yandexApiKeys.serializers import YandexAPIKeySerializer


class ActiveYandexAPIKeyList(ViewSet):
    """
    Получить активный ключ яндекса для работы карт
    """
    
    def list(self, request, format=None):
        yandexActiveKey = YandexAPIKey.objects.filter(
            active=True
        ).first()
        serializer = YandexAPIKeySerializer(yandexActiveKey)
        return Response(serializer.data)