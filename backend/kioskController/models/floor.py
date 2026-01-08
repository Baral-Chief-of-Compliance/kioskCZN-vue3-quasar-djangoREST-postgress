from django.db import models

from kioskController.models.personal_center import PC


class Floor(models.Model):
    """Этаж кадрового центра"""

    f_pc = models.ForeignKey(verbose_name="Кадровый центр", to=PC, on_delete=models.CASCADE)
    f_number = models.IntegerField(verbose_name="Номер этажа")
    f_building_img = models.ImageField(verbose_name="Схема этажа", upload_to='floor_imgs/')

    def __str__(self) -> str:
        return f'Этаж {self.f_number} {self.pc}'
    
    class Meta:
        verbose_name = 'Этаж КЦ'
        verbose_name_plural = 'Этажи КЦ'