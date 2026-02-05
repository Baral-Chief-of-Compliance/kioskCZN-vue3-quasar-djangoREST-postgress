from django.contrib import admin

from version_app.models import Version
# Register your models here.


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    pass