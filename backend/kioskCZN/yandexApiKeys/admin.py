from django.contrib import admin

from yandexApiKeys.models import YandexAPIKey


@admin.register(YandexAPIKey)
class YandexAPIKeyAdmin(admin.ModelAdmin):
    fields = ('name', 'date', 'active')
    readonly_fields = ('date',)