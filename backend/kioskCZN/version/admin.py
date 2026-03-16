from django.contrib import admin

from version.models import Version

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

    def has_add_permission(self, request):
        return False  # Убирает кнопку "Добавить"
    
    def has_delete_permission(self, request, obj=None):
        return False  # Убирает возможность удаления