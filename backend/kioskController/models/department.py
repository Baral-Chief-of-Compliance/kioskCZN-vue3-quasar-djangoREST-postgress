from django.db import models

from kioskController.models.personal_center import PC


class Department(models.Model):
    """Отдел кадрового центра"""

    dep_pc = models.ForeignKey(verbose_name='Кадровый центр', to=PC, on_delete=models.CASCADE)
    dep_name = models.CharField(verbose_name='Наименование кадрового центра', max_length=256)
    dep_priority = models.PositiveIntegerField(verbose_name='Порядок отображения', default=999)
    dep_visible = models.BooleanField(verbose_name='Статус отображения', default=False)

    def __str__(self) -> str:
        return self.dep_name
    
    class Meta:
        verbose_name = 'Отдел кадрового центра'
        verbose_name_plural = 'Отделы кадровых центров'