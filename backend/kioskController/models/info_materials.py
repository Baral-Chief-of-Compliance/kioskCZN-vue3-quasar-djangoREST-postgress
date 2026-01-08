import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class InfoMaterials(models.Model):
    """Информационные материалы"""

    im_name = models.TextField(verbose_name="Наименование информационного материала")
    im_file = models.FileField(verbose_name="Файл информационного материала", upload_to='info_materials/')
    im_priority = models.PositiveIntegerField(verbose_name="Порядок отображения", default=999)

    def __str__(self) -> str:
        return self.im_name
    
    class Meta:
        verbose_name = 'Информационный материал КЦ'
        verbose_name_plural = 'Информационные материалы КЦ'


@receiver(post_delete, sender=InfoMaterials)
def auto_delete_info_materials_file(sender, instance, **kwargs):
    """
    Удаление файла информационного материала при удалении InfoMaterials из базы
    """

    if instance.im_file:
        if os.path.isFile(instance.im_file.path):
            os.remove(instance.im_file.path)