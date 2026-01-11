from datetime import datetime, timedelta

from django.db import models

from kioskController.models import PC
from .glossary import PC_NAME, TITEL_NAME



def get_datetime_now():
    """Получить текущее время"""
    return datetime.now()


def get_datetime_next():
    """Получить текущее время на час больше"""
    return datetime.now() + timedelta(hours=1)

class Event(models.Model):
    """Мероприятие в КЦ"""



    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=TITEL_NAME, max_length=512)
    discription = models.TextField(verbose_name='Описание', blank=True, null=True)
    date_start = models.DateField(verbose_name='Дата начала', default=get_datetime_now)
    time_start = models.TimeField(verbose_name='Время начала', default=get_datetime_now)
    date_end = models.DateField(verbose_name='Дата окончания', default=get_datetime_next)
    time_end = models.TimeField(verbose_name='Время окончания', default=get_datetime_next)

    def __str__(self) -> str:
        return f'"{self.name}" в {self.pc}'
    
    class Meta:
        verbose_name = 'Мероприятие в КЦ'
        verbose_name_plural = 'Мероприятия в КЦ'
        db_table = 'event'