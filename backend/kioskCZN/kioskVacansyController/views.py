from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from kioskVacansyController.serializers import DistrictsSerializer
from kioskVacansyController.models import Districts


class DistrictsViewSet(viewsets.ModelViewSet):
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'