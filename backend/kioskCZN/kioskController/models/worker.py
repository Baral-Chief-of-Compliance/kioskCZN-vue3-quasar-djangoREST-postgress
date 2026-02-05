from django.db import models

from kioskController.models import Post, Room, Department, Service
from .glossary import DISPLAY_STATUS_NAME


class Worker(models.Model):
    """Сотрудник кадрового центра"""

    id = models.PositiveIntegerField(
        primary_key=True, verbose_name='Id сотрудника в телефонном справочнике')
    
    fio = models.CharField(verbose_name='ФИО', max_length=512)
    room = models.ForeignKey(verbose_name='Кабинет', to=Room, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=128, blank=True, null=True)
    date_get_info = models.DateField(verbose_name='Дата обновления информации', auto_now=True)
    absent = models.BooleanField(verbose_name='Статус отсутствия', default=False)
    email = models.CharField(verbose_name='Email', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Сотрудник КЦ'
        verbose_name_plural = 'Сотрудники КЦ'
        db_table = 'worker'


class WorkerInDepartment(models.Model):
    """Сотрудник в отделе"""
    worker = models.ForeignKey(verbose_name='Сотрудник', to=Worker, on_delete=models.CASCADE)
    dep = models.ForeignKey(verbose_name='Отдел', to=Department, on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Должность в отделе', to=Post, on_delete=models.SET_NULL, null=True, blank=True)
    head_of_dep = models.BooleanField(verbose_name='Глава отдела', default=False)
    services = models.ManyToManyField(verbose_name='Услуги сотрудника', to=Service, blank=True)
    visible = models.BooleanField(verbose_name=DISPLAY_STATUS_NAME, default=False)


    def __str__(self):
        return f'{self.worker} отдела {self.dep}'
    
    class Meta:
        verbose_name = 'Сотрудник отдела КЦ'
        verbose_name_plural = 'Сотрудники отделов КЦ'
        db_table = 'worker_in_department'

    