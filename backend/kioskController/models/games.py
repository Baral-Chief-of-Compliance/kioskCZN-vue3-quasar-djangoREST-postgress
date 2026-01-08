from django.db import models

from kioskController.models.personal_center import PC


class Game(models.Model):
    """Игры в информационном киоске"""
    g_name = models.CharField(verbose_name='Наименование игры', max_length=128)
    g_priority = models.PositiveIntegerField(verbose_name='Порядок отображения игры', default=999)

    def __str__(self) -> str:
        return self.g_name

    class Meta:
        verbose_name = 'Игра КЦ'
        verbose_name_plural = 'Игры КЦ'

class GameUrl(models.Model):
    """Ссылка на игру для КЦ"""
    gu_pc = models.ForeignKey(verbose_name='Кадровый центра', to=PC, on_delete=models.CASCADE)
    gu_game = models.ForeignKey(verbose_name='Игра', to=Game, on_delete=models.CASCADE)
    gu_url = models.CharField(verbose_name='Ссылка на игру', max_length=256)

    def __str__(self) -> str:
        return f'Ссылка для игры "{self.gu_game}" в {self.gu_pc}'
    
    class Meta:
        verbose_name = 'Ссылка на игру для КЦ'
        verbose_name_plural = 'Ссылки на игру для КЦ'


class GameVisibleStatus(models.Model):
    """Статус отображения игры для Кадрового центра"""
    gvs_pc = models.ForeignKey(verbose_name='Кадровый центр', to=PC, on_delete=models.CASCADE)
    gvs_game = models.ForeignKey(verbose_name='Игра', to=Game, on_delete=models.CASCADE)
    gvs_status = models.BooleanField(verbose_name='Статус отображения', default=True)

    def __str__(self) -> str:
        return f'Статус отображения игры "{self.gvs_game}" в {self.gvs_pc}'
    
    class Meta:
        verbose_name = 'Статус отображения игры в КЦ'
        verbose_name_plural = 'Статусы отображения игр в КЦ'