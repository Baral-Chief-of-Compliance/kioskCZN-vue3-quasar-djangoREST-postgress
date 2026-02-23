from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from kioskController.models import APIkey,\
Department, Event, Floor, Game, GameUrl, GameVisibleStatus,\
InfoMaterials, PCParentOrganization, PCParentOrganizationPhone,\
PCParentOrganizationAddress, PCParentOrganizationEmail, PCHeadInfo,\
PCHeadInfoPhone, PCHeadInfoTimeTable, PC, PCSocialNetworks,\
PCAddress, PCPhone, PCEmail, PCSites, PCTimeTable, Post,\
Room, Service, Worker, WorkerInDepartment, PCHeadInfoEmail, ShowDepartmentInOtherPC


admin.site.site_header = 'Киоск ЦЗН МО | Админ-панель'  # Отображается вверху
admin.site.site_title = 'Киоск ЦЗН МО | Админ-панель'  # Title страницы
admin.site.index_title = 'Киоск ЦЗН МО | Админ-панель'  # На главной после входа


@admin.register(APIkey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "date_create",
        "active",
    ]
    readonly_fields = [
        "api_key",
    ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
       "name",
       "priority" ,
       "visible",
       "pc"
    ]
    search_fields = [
        "name",
    ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]

    list_display = [
        "name",
        "pc",
        "date_start"
    ]

    search_fields = [
        "name",
    ]


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(GameUrl)
class GameUrlAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]


@admin.register(GameVisibleStatus)
class GameVisibleStatusAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]


@admin.register(InfoMaterials)
class InfoMaterialsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "priority",
    ]

    search_fields = [
        "name",
    ]


@admin.register(PCParentOrganization)
class PCParentOrganizationAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]


@admin.register(PCParentOrganizationPhone)
class PCParentOrganizationPhoneAdmin(admin.ModelAdmin):
    list_display = [
        "org",
        "phone",
    ]
    search_fields = [
        "org",
    ]


@admin.register(PCParentOrganizationAddress)
class PCParentOrganizationAddressAdmin(admin.ModelAdmin):
    list_display = [
        "org",
        "address",
    ]
    search_fields = [
        "org",
    ]


@admin.register(PCParentOrganizationEmail)
class PCParentOrganizationEmailAdmin(admin.ModelAdmin):
    list_display = [
        "org",
        "email",
    ]
    search_fields = [
        "org",
    ]


@admin.register(PCHeadInfo)
class PCHeadInfoAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
        "pc",
        "worker",
        "name",
    ]


@admin.register(PCHeadInfoPhone)
class PCHeadInfoPhoneAdmin(admin.ModelAdmin):
    list_filter = [
        "pc_head_info__pc",
    ]
    list_display = [
        "pc_head_info",
        "phone",
    ]

@admin.register(PCHeadInfoEmail)
class PCHeadInfoEmailAdmin(admin.ModelAdmin):
    list_filter = [
        "pc_head_info__pc",
    ]
    list_display = [
        "pc_head_info",
        "email",
    ]

@admin.register(PCHeadInfoTimeTable)
class PCHeadInfoTimeTableAdmin(admin.ModelAdmin):
    list_filter = [
        "pc_head_info__pc",
    ]
    list_display = [
        "pc_head_info",
        "day_of_week",
        "start_time",
        "end_time"
    ]


@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    list_display = [
      "name",
      "url_path",
      "id_parsing",
    ]


@admin.register(PCSocialNetworks)
class PCSocialNetworksAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
       "pc",
       "name",
       "link"
    ]


@admin.register(PCAddress)
class PCAddressAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
        "pc",
        "address",
    ]


@admin.register(PCPhone)
class PCPhoneAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
        "pc",
        "name",
        "phone",
    ]

@admin.register(PCEmail)
class PCEmailAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
        "pc",
        "name",
        "email",
    ]


@admin.register(PCSites)
class PCSitesAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
        "pc",
        "name",
        "url",
    ]

@admin.register(PCTimeTable)
class PCTimeTableAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
        "pc",
        "day_of_week",
        "day_off",
        "time_start",
        "time_end"
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "priority",
    ]

    search_fields = [
        "name",
    ]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_filter = [
        "pc",
    ]
    list_display = [
        "name",
        "floor",
        "pc",
        "visible",
    ]

    search_fields = [
        "name",
    ]


# Подключение CKEditor для описания услуг
class ServiceDescriptionForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Service
        fields = '__all__'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceDescriptionForm


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    readonly_fields = ['date_get_info']

    list_display = [
        "fio",
        "email",
        "absent",
        "date_get_info",
    ]

    search_fields = [
        "fio",
    ]



@admin.register(WorkerInDepartment)
class WorkerInDepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ['date_get_info']

    search_fields = [
        "worker__fio",
    ]

    list_display = [
        "worker__fio",
        "dep",
        "post",
        "head_of_dep",
        "date_get_info",
        "visible"
    ]

    list_filter = [
        "dep__pc",
    ]

@admin.register(ShowDepartmentInOtherPC)
class ShowDepartmentInOtherPCAdmin(admin.ModelAdmin):
    list_display = [
        "pc",
        "dep",
    ]

    list_filter = [
        "pc",
    ]

    search_fields = [
        "dep",
    ]