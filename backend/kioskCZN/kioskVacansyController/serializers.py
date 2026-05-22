from rest_framework import serializers
from django.db.models import Sum

from kioskVacansyController.models import Districts, Vacansy,\
UserFromMaxMiniApp, FavoriteVacansy, MaxUserResume, VacancyResponseFromUserMax


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
            'fullCompanyName',
            'vacancyUrl'
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


class UserFromMaxMiniAppSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя Mini App в Max"""

    class Meta:
        model = UserFromMaxMiniApp
        fields = [
            'id'
        ]


class MaxUserResumeSerializer(serializers.ModelSerializer):
    """Сериализатор для резюме пользователя Mini App в Max"""

    class Meta:
        models = MaxUserResume
        fields = '__all__'


class VacancyResponseFromUserMaxSerializer(serializers.ModelSerializer):
    """Сериализатор для Отклика пользователя Max Mini App на вакансию"""

    class Meta:
        models = VacancyResponseFromUserMax
        fields = '__all__'


class FavoriteVacansySerializer(serializers.ModelSerializer):
    """Сериализатор для избранных вакансий"""

    class Meta:
        model = FavoriteVacansy
        fields = '__all__'

class FavoriteVacansyListSerializer(serializers.ModelSerializer):
    """Сериализатор для list избранных вакансий"""

    vacancy_name = serializers.CharField(source='vacancy.vacancyName', read_only=True)
    salary = serializers.CharField(source='vacancy.salary', read_only=True)
    vacancy_address = serializers.CharField(source='vacancy.vacancyAddress', read_only=True)
    salary_max = serializers.IntegerField(source='vacancy.salaryMax', read_only=True)
    salary_min = serializers.IntegerField(source='vacancy.salaryMin', read_only=True)
    work_places = serializers.IntegerField(source='vacancy.workPlaces', read_only=True)
    full_company_name = serializers.CharField(source='vacancy.fullCompanyName', read_only=True)
    vacancy_url = serializers.CharField(source='vacancy.vacancyUrl', read_only=True)

    class Meta:
        model = FavoriteVacansy
        fields = [
            'id',
            'vacancy',
            'user',
            'vacancy_name',
            'salary',
            'vacancy_address',
            'salary_max',
            'salary_min',
            'work_places',
            'full_company_name',
            'vacancy_url'
        ]