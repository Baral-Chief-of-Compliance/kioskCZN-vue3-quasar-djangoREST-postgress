from django.db import models

from kioskController.models.post import Post
from kioskController.models.room import Room
from kioskController.models.department import Department
from kioskController.models.service import Service


class Worker(models.Model):
    """Сотрудник кадрового центра"""

    w_id = models.PositiveIntegerField(
        primary_key=True, verbose_name='Id сотрудника в телефонном справочнике')
    
    w_fio = models.CharField(verbose_name='ФИО', max_length=512)
    w_room = models.ForeignKey(verbose_name='Кабинет', to=Room, on_delete=models.CASCADE, blank=True, null=True)
    w_phone = models.CharField(verbose_name='Номер телефона', max_length=128, blank=True, null=True)
    w_date_get_info = models.DateField(verbose_name='Дата обновления информации', auto_now=True)
    w_absent = models.BooleanField(verbose_name='Статус отсутствия', default=False)

    def __str__(self):
        return self.w_fio
    
    class Meta:
        verbose_name = 'Сотрудник КЦ'
        verbose_name_plural = 'Сотрудники КЦ'


class WorkerInDepartment(models.Model):
    """Сотрудник в отделе"""
    wid_worker = models.ForeignKey(verbose_name='Сотрудник', to=Worker, on_delete=models.CASCADE)
    wid_dep = models.ForeignKey(verbose_name='Отдел', to=Department, on_delete=models.CASCADE)
    wid_post = models.ForeignKey(verbose_name='Должность в отделе', to=Post, on_delete=models.SET_NULL, null=True, blank=True)
    wid_head_of_dep = models.BooleanField(verbose_name='Глава отдела', default=False)
    wid_services = models.ManyToManyField(verbose_name='Услуги сотрудника', to=Service, null=True, blank=True)

    def __str__(self):
        return f'{self.wid_worker} отдела {self.wid_dep}'
    
    class Meta:
        verbose_name = 'Сотрудник отдела КЦ'
        verbose_name_plural = 'Сотрудники отделов КЦ'

    