from django.db import models

from kioskVacansyController.models import UserFromMaxMiniApp


class PreRegistration(models.Model):
    """Пререгистрация"""
    name = models.CharField(verbose_name='Наименование пререгистрации', max_length=256)
    show = models.BooleanField(verbose_name='Отображение на сайте', default=True)
    pre_registration_code = models.CharField(verbose_name='Код пререгистрации', max_length=256)
    czn_code = models.CharField(verbose_name='Код отделения', max_length=128, unique=True)
    ip_addr = models.CharField(verbose_name='Ip addr сервера очереди', max_length=128)
    port = models.PositiveIntegerField(verbose_name='Порт сервера очереди')
    prioritet = models.PositiveIntegerField(verbose_name='Приоритет', default=999)
    address = models.TextField(
        verbose_name='Адрес',
        default='Адрес'
    )

    def __str__(self) -> str:
        return f"Пререгистрация {self.name}"
    
    class Meta:
        verbose_name = 'Пререгистрация'
        verbose_name_plural = 'Пререгистрации'
        db_table = 'pre_registration'


class PreRegistrationLog(models.Model):
    """Лог пререгистрации"""

    pre_registration = models.ForeignKey(
        verbose_name='Пререгистрация',
        to=PreRegistration,
        on_delete=models.CASCADE
    )

    error = models.BooleanField(
        verbose_name='Статус ошибки',
        default=False
    )

    content = models.TextField(
        verbose_name='Содержание лога'
    )

    date = models.DateTimeField(
        verbose_name='Дата лога',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f'Лог пререгистрации {self.pre_registration.name}'

    class Meta:
        verbose_name = 'Лог пререгистрации'
        verbose_name_plural = 'Логи пререгистрации'
        db_table = 'pre_registration_log'


class PreRegistrationRecord(models.Model):
    """Запись на пререгистрацию"""
    pre_registration = models.ForeignKey(
        verbose_name='Пререгистрация',
        to=PreRegistration,
        on_delete=models.CASCADE
    )

    max_user = models.ForeignKey(
        to=UserFromMaxMiniApp,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь с MAX',
        help_text='Данное поле нужно если пользователь записывался через Mini App в максе',
        null=True,
        blank=True
    )


    date_time = models.DateTimeField(
        verbose_name='Дата и время записи'
    )

    email = models.EmailField(
        verbose_name="Email записавашегоса",
        null=True,
        blank=True
    )

    code = models.BigIntegerField(
        verbose_name='Код пререгистрации',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f'Запись в {self.pre_registration.name} на {self.date_time}'
    

    class Meta:
        verbose_name = 'Запись на пререгистрацию'
        verbose_name_plural = 'Записи на пререгистрации'
        db_table = 'pre_registration_record'