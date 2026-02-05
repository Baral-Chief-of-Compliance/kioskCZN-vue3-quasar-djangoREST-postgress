from django.contrib import admin

from kioskController.models import APIkey,\
Department, Event, Floor, Game, GameUrl, GameVisibleStatus,\
InfoMaterials, PCParentOrganization, PCParentOrganizationPhone,\
PCParentOrganizationAddress, PCParentOrganizationEmail, PCHeadInfo,\
PCHeadInfoPhone, PCHeadInfoTimeTable, PC, PCSocialNetworks,\
PCAddress, PCPhone, PCEmail, PCSites, PCTimeTable, Post,\
Room, Service, Worker, WorkerInDepartment
# Register your models here.


@admin.register(APIkey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "date_create",
        "active"
    ]
    readonly_fields = [
        "api_key"
    ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(GameUrl)
class GameUrlAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(GameVisibleStatus)
class GameVisibleStatusAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(InfoMaterials)
class InfoMaterialsAdmin(admin.ModelAdmin):
    pass


@admin.register(PCParentOrganization)
class PCParentOrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(PCParentOrganizationPhone)
class PCParentOrganizationPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(PCParentOrganizationAddress)
class PCParentOrganizationAddressAdmin(admin.ModelAdmin):
    pass 


@admin.register(PCParentOrganizationEmail)
class PCParentOrganizationEmailAdmin(admin.ModelAdmin):
    pass


@admin.register(PCHeadInfo)
class PCHeadInfoAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(PCHeadInfoPhone)
class PCHeadInfoPhoneAdmin(admin.ModelAdmin):
    list_filter = [
        "pc_head_info"
    ]

@admin.register(PCHeadInfoTimeTable)
class PCHeadInfoTimeTableAdmin(admin.ModelAdmin):
    list_filter = [
        "pc_head_info"
    ]


@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    pass


@admin.register(PCSocialNetworks)
class PCSocialNetworksAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(PCAddress)
class PCAddressAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(PCPhone)
class PCPhoneAdmin(admin.ModelAdmin):
    list_filter = [
        "pc"
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_filter = [
        "floor__pc"
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkerInDepartment)
class WorkerInDepartmentAdmin(admin.ModelAdmin):
    list_filter = [
        "dep"
    ]