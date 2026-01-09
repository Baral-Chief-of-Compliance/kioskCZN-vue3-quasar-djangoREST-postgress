from django.db import models

from .glossary import PC_NAME
from kioskController.models.personal_center import PC


class Floor(models.Model):
    """Этаж кадрового центра"""

    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="Номер этажа")
    building_img = models.ImageField(verbose_name="Схема этажа", upload_to='floor_imgs/')

    def __str__(self) -> str:
        return f'Этаж {self.number} {self.pc}'
    
    class Meta:
        verbose_name = 'Этаж КЦ'
        verbose_name_plural = 'Этажи КЦ'