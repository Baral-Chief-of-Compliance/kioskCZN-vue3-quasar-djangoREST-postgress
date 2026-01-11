from datetime import datetime

from django.db import models

from kioskController.models import Worker, PC
from .glossary import PC_NAME, TITEL_NAME, DISPLAY_ORDER_NAME,\
PC_HEAD_INFO_NAME, DAY_OF_WEEK


class PCHeadInfo(models.Model):
    """Рукводитель КЦ"""

    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    worker = models.ForeignKey(verbose_name='Сотрудник КЦ', to=Worker, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=TITEL_NAME, max_length=512)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)
    photo = models.ImageField(verbose_name='Фото руководителя КЦ', upload_to='pc_head_info/', blank=True, null=True)

    def __str__(self) -> str:
        return f'Руководитель {self.pc} {self.worker.fio}'
    
    class Meta:
        verbose_name = 'Руководитель КЦ'
        verbose_name_plural = 'Руководители КЦ'
        db_table = 'pc_head_info'


class PCHeadInfoPhone(models.Model):
    """Номер телефона руководителя КЦ"""
    pc_head_info = models.ForeignKey(verbose_name=PC_HEAD_INFO_NAME, to=PCHeadInfo, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телфона', max_length=64)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)

    def __str__(self) -> str:
        return f'Телефон {self.pc_head_info}'
    
    class Meta:
        verbose_name = 'Номер телефона руководителя КЦ'
        verbose_name_plural = 'Номера телефонов руководителей КЦ'
        db_table = 'pc_head_info_phone'


class PCHeadInfoTimeTable(models.Model):
    """Часы приема руководителя КЦ"""

    pc_head_info = models.ForeignKey(verbose_name=PC_HEAD_INFO_NAME, to=PCHeadInfo, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(verbose_name='День недели', choices=DAY_OF_WEEK)
    start_time = models.TimeField(verbose_name='Время начала приема', default=datetime.now)
    end_time = models.TimeField(verbose_name='Время окончания приема', default=datetime.now)

    def __str__(self) -> str:
        return f'Часы приема в {DAY_OF_WEEK[self.day_of_week][1]} у {self.pc_head_info}'
    
    class Meta:
        verbose_name = 'Часы приема руководителя КЦ'
        verbose_name_plural = 'Часы приемов руководителей КЦ'
        db_table = 'pc_head_info_time_table'