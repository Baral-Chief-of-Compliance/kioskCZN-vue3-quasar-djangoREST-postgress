from django.contrib import admin

from kioskVacansyController.models import Vacansy, Districts,\
UserFromMaxMiniApp, FavoriteVacansy, VacancyResponseFromUserMax,\
MaxUserResume


@admin.register(Districts)
class DistrictsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'min_code',
        'max_code',
    ]

    search_fields = [
        'name',
    ]


@admin.register(Vacansy)
class VacansyAdmin(admin.ModelAdmin):
    list_display = [
        'vacancyName',
        'salaryMin',
        'salaryMax',
        'workPlaces'
    ]

    search_fields = [
        'vacancyName',
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Для существующих объектов
            # Получаем все поля модели
            return [field.name for field in self.opts.local_fields]
        return []  # Для новых объектов поля редактируемы
    

@admin.register(UserFromMaxMiniApp)
class UserFromMaxMiniAppAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'start_use_date'
    )

    search_fields = (
        'id', 
    )
    
    readonly_fields = (
        'start_use_date',
    )


@admin.register(MaxUserResume)
class MaxUserResumeAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'date'
    )

    search_fields = (
        'user__id', 'name'
    )

    readonly_fields = (
        'date',
    )


@admin.register(VacancyResponseFromUserMax)
class VacancyResponseFromUserMaxAdmin(admin.ModelAdmin):
    list_display = (
        'resume', 'date', 'vacancy_url'
    )

    search_fields = (
        'resume__user__id', 'vacancy_url'
    )

    readonly_fields = (
        'date',
    )


@admin.register(FavoriteVacansy)
class FavoriteVacansyAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'vacancy'
    )

    search_fields = (
        'user__id',
        'vacancy__id',
        'vacancy__vacancyName'
    )