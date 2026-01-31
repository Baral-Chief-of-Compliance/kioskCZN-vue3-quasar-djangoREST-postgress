from datetime import datetime

from django.db import models

from kioskController.models import  PCParentOrganization
from .glossary import PC_NAME, DISPLAY_ORDER_NAME,\
TITEL_NAME, PC_PARENT_OGR, DAY_OF_WEEK


class PC(models.Model):
    """Кадровый центр"""
    name = models.CharField(verbose_name=TITEL_NAME, max_length=256, unique=True)
    parent_org = models.ForeignKey(verbose_name=PC_PARENT_OGR, to=PCParentOrganization, on_delete=models.CASCADE, blank=True, null=True)
    url_path= models.CharField(verbose_name="Наименование url пути", unique=True)
    id_parsing = models.IntegerField(verbose_name="Id идентификации КЦ в телефонном справочнике", unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Кадровый центр'
        verbose_name_plural = 'Кадровые центры'
        db_table = 'pc'


class PCSocialNetworks(models.Model):
    """Социальные сети КЦ"""

    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=TITEL_NAME, max_length=512)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)
    link = models.CharField(verbose_name='Ссылка на группу в соц. сети', max_length=512)
    qr_code = models.ImageField(verbose_name='QR code', upload_to='social_networks/', blank=True, null=True)

    def __str__(self) -> str:
        return f'соц. сеть "{self.name}" {self.pc}'

    class Meta:
        verbose_name = 'Информация о социальной сети КЦ'
        verbose_name_plural = 'Информация о социальных сетях КЦ'
        db_table = 'pc_social_networks'


class PCAddress(models.Model):
    """Адреса КЦ"""

    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Адреса КЦ', max_length=512)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)

    def __str__(self) -> str:
        return f'адрес {self.pc}'
    
    class Meta:
        verbose_name = 'Адрес КЦ'
        verbose_name_plural = 'Адреса КЦ'
        db_table = 'pc_address'


class PCPhone(models.Model):
    """Телефон КЦ"""

    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=TITEL_NAME, max_length=256, blank=True, null=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=64)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)

    def __str__(self) -> str:
        return f'номер "{self.phone}" {self.pc}'
    
    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'
        db_table = 'pc_phone'


class PCEmail(models.Model):
    """Электронная почта КЦ"""

    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=TITEL_NAME, max_length=256, blank=True, null=True)
    email = models.EmailField(verbose_name='Email')
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)

    def __str__(self) -> str:
        return f'email "{self.email}" {self.pc}'
    
    class Meta:
        verbose_name = 'Электронная почта КЦ'
        verbose_name_plural = 'Электронные почты КЦ'
        db_table = 'pc_email'


class PCSites(models.Model):
    """Сайты КЦ"""
    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=TITEL_NAME, max_length=256, null=True, blank=True)
    url = models.CharField(verbose_name='Ссылка на сайт', max_length=256)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)
    qr_code_img = models.ImageField(verbose_name='Qr код', upload_to='pc_info_qr_codes/', blank=True, null=True)

    def __str__(self) -> str:
        return f'сайт "{self.url}" {self.pc}'
    
    class Meta:
        verbose_name = 'Сайт КЦ'
        verbose_name_plural = 'Сайты КЦ'
        db_table = 'pc_sites'




class PCTimeTable(models.Model):
    """Расписание КЦ"""
    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(verbose_name='День недели', default=0, choices=DAY_OF_WEEK)
    day_off = models.BooleanField(verbose_name='Выходной день', default=False)
    time_start = models.TimeField(verbose_name='Время начала рабочего дня', default=datetime.now, blank=True, null=True)
    time_end = models.TimeField(verbose_name='Время окончания рабочего дня', default=datetime.now, blank=True, null=True)

    def __str__(self) -> str:
        return f'Расписание для {DAY_OF_WEEK[self.day_of_week][1]} {self.pc}'
    
    class Meta:
        verbose_name = 'Расписание КЦ'
        verbose_name_plural = 'Расписания КЦ'
        db_table = 'pc_time_table'