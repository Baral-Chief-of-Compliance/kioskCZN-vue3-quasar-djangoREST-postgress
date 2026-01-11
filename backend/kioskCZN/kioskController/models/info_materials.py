import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .glossary import DISPLAY_ORDER_NAME, TITEL_NAME


class InfoMaterials(models.Model):
    """Информационные материалы"""

    name = models.TextField(verbose_name=TITEL_NAME)
    file = models.FileField(verbose_name="Файл информационного материала", upload_to='info_materials/')
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Информационный материал КЦ'
        verbose_name_plural = 'Информационные материалы КЦ'
        db_table = 'info_material'


@receiver(post_delete, sender=InfoMaterials)
def auto_delete_info_materials_file(sender, instance, **kwargs):
    """
    Удаление файла информационного материала при удалении InfoMaterials из базы
    """

    if instance.file:
        if os.path.isFile(instance.file.path):
            os.remove(instance.file.path)