from rest_framework import serializers
from django.db.models import Sum

from kioskVacansyController.models import Districts, Vacansy


class VacansySerializer(serializers.ModelSerializer):
    """Сериализатор вакансий"""

    class Meta:
        model = Vacansy
        fields = '__all__'


class VacansyInListSerializer(serializers.ModelSerializer):
    """Сериализатор вакансий для просмотра в списке"""

    class Meta:
        model = Vacansy
        fields = [
            'id',
            'vacancyName',
            'vacancyAddress',
            'salary',
            'salaryMin',
            'salaryMax',
            'workPlaces',
            'fullCompanyName'
        ]


class DistrictsSerializer(serializers.ModelSerializer):
    """Сериализатор района"""

    count_vacansy = serializers.SerializerMethodField('get_count_vacansy')

    def get_count_vacansy(self, obj: Districts):
        result = Vacansy.objects.filter(
            addressCode__gte=obj.min_code,
            addressCode__lte=obj.max_code
        ).aggregate(
            total_workplaces = Sum('workPlaces')
        )

        return result['total_workplaces'] or 0

    class Meta:
        model = Districts
        fields = [
            'id',
            'name',
            'min_code',
            'max_code',
            'count_vacansy'
        ]


class DistrictsDetailSerializer(serializers.ModelSerializer):
    """Сериализатор района"""

    vacansy = serializers.SerializerMethodField('get_vacansy')

    def get_vacansy(self, obj: Districts):
        result = Vacansy.objects.filter(
            addressCode__gte=obj.min_code,
            addressCode__lte=obj.max_code
        )

        return VacansyInListSerializer(result, many=True).data


    class Meta:
        model = Districts
        fields = [
            'id',
            'name',
            'min_code',
            'max_code',
            'vacansy'
        ]