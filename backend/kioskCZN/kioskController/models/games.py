from django.db import models

from .glossary import PC_NAME, DISPLAY_ORDER_NAME, DISPLAY_STATUS_NAME, TITEL_NAME
from kioskController.models import PC


class Game(models.Model):
    """Игры в информационном киоске"""
    name = models.CharField(verbose_name=TITEL_NAME, max_length=128)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Игра КЦ'
        verbose_name_plural = 'Игры КЦ'

class GameUrl(models.Model):
    """Ссылка на игру для КЦ"""
    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    game = models.ForeignKey(verbose_name='Игра', to=Game, on_delete=models.CASCADE)
    url = models.CharField(verbose_name='Ссылка на игру', max_length=256)

    def __str__(self) -> str:
        return f'Ссылка для игры "{self.game}" в {self.pc}'
    
    class Meta:
        verbose_name = 'Ссылка на игру для КЦ'
        verbose_name_plural = 'Ссылки на игру для КЦ'
        db_table = 'game'


class GameVisibleStatus(models.Model):
    """Статус отображения игры для Кадрового центра"""
    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    game = models.ForeignKey(verbose_name='Игра', to=Game, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name=DISPLAY_STATUS_NAME, default=True)

    def __str__(self) -> str:
        return f'Статус отображения игры "{self.game}" в {self.pc}'
    
    class Meta:
        verbose_name = 'Статус отображения игры в КЦ'
        verbose_name_plural = 'Статусы отображения игр в КЦ'
        db_table = 'game_visible_status'