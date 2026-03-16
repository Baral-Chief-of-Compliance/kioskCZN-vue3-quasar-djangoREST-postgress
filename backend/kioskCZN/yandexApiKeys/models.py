from django.db import models

from kioskController.models.glossary import TITEL_NAME


class YandexAPIKey(models.Model):
    name = models.CharField(verbose_name=TITEL_NAME, max_length=256)
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    key = models.TextField(verbose_name='API ключ', help_text='Ключ получить можно с https://developer.tech.yandex.ru/')
    active = models.BooleanField(verbose_name='Активен', default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Yandex API ключ'
        verbose_name_plural = 'Yandex API ключи'