from django.contrib import admin

from pre_registration.models import PreRegistration,\
    PreRegistrationLog,  PreRegistrationRecord


@admin.register(PreRegistration)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'show',
        'czn_code',
        'ip_addr',
        'port'
    ]

    search_fields = [
        'name',
        'ip_addr'
    ]

    list_filter = [
        'show',
    ]


@admin.register(PreRegistrationLog)
class PreRegistrationLogAdmin(admin.ModelAdmin):
    list_display = [
        'pre_registration',
        'error',
        'date'
    ]

    search_fields = [
        'pre_registration__name',
        'pre_registration__ip_addr'
    ]

    list_filter = [
        'pre_registration',
        'error'
    ]

    readonly_fields = [
        'date',
    ]


@admin.register(PreRegistrationRecord)
class PerRegistrationRecordAdmin(admin.ModelAdmin):
    list_display = [
        'pre_registration',
        'max_user',
        'email',
        'date_time',
        'code'
    ]

    search_fields = [
        'pre_registration__name',

    ]

    list_filter = [
        'pre_registration',
    ]

    readonly_fields = [
        'date_time',
    ]