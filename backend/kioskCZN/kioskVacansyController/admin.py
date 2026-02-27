from django.contrib import admin

from kioskVacansyController.models import Vacansy, Districts


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
