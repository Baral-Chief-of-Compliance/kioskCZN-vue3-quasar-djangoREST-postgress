from django.db import models


class Service(models.Model):
    """Услуга Кадрового центра"""

    s_name = models.TextField(verbose_name="Наименование услуги КЦ")
    s_priority = models.PositiveIntegerField(verbose_name="Порядок отображения услуги", default=999)


    def __str__(self) -> str:
        return self.s_name
    
    class Meta:
        verbose_name = 'Услуга КЦ'
        verbose_name_plural = 'Услуги КЦ'