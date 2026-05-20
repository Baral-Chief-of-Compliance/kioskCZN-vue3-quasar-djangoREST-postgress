from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as rest_filter
from rest_framework.filters import OrderingFilter

from kioskVacansyController.serializers import DistrictsSerializer, DistrictsDetailSerializer,\
VacansyInListSerializer, VacansySerializer, UserFromMaxMiniAppSerializer,\
FavoriteVacansySerializer, FavoriteVacansyListSerializer
from kioskVacansyController.models import Districts, Vacansy, UserFromMaxMiniApp,\
FavoriteVacansy
from kioskVacansyController.paginators import CustomPageNumberPagination


class VacansyFilter(rest_filter.FilterSet):
    address_code__gte = rest_filter.NumberFilter(field_name='addressCode', lookup_expr='gte')
    address_code__lte = rest_filter.NumberFilter(field_name='addressCode', lookup_expr='lte')
    search = rest_filter.CharFilter(field_name='vacancyName', lookup_expr='icontains')

    class Meta:
        model = Vacansy
        fields = ['addressCode', 'search']


class DistrictsViewSet(viewsets.ModelViewSet):
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
   

class VacansyViewSet(viewsets.ModelViewSet):
    queryset = Vacansy.objects.all()
    serializer_class = VacansyInListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = VacansyFilter
    pagination_class = CustomPageNumberPagination
    ordering_fields = ['vacancyName', 'salaryMax', 'salaryMin']  # Поля для сортировки
    ordering = ['vacancyName']  # Сортировка по умолчанию

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VacansySerializer
        else:
            return self.serializer_class
        
    
class UserFromMaxMiniAppViewSet(viewsets.ModelViewSet):
    queryset = UserFromMaxMiniApp.objects.all()
    serializer_class = UserFromMaxMiniAppSerializer


class FavoriteVacansyViewSet(viewsets.ModelViewSet):
    queryset = FavoriteVacansy.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    serializer_class = FavoriteVacansySerializer
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'list':
            return FavoriteVacansyListSerializer
        else:
            return FavoriteVacansySerializer