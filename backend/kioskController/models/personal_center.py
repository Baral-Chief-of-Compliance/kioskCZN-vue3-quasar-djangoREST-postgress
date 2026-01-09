from datetime import datetime

from django.db import models
from kioskController.models.worker import Worker
from .glossary import PC_NAME, DISPLAY_ORDER_NAME, PC_HEAD_INFO_NAME, TITEL_NAME


class PC(models.Model):
    """Кадровый центр"""
    name = models.CharField(verbose_name=TITEL_NAME, max_length=256)
    url_path= models.CharField(verbose_name="Наименование url пути")
    id_parsing = models.IntegerField(verbose_name="Id идентификации КЦ в телефонном справочнике")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Кадровый центр'
        verbose_name_plural = 'Кадровые центры'


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


DAY_OF_WEEK = (
    (
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье')
    )
)

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