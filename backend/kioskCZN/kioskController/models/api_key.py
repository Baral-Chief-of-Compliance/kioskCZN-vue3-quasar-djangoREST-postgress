import secrets

from django.db import models

from .glossary import TITEL_NAME


def generate_api_key() -> str:
    """Сгенирировать API ключ"""
    return secrets.token_urlsafe(32)


class APIkey(models.Model):
    """API ключи для взаимодействия"""

    name = models.CharField(verbose_name=TITEL_NAME, max_length=128)
    api_key = models.CharField(verbose_name='API ключ', default=generate_api_key, max_length=128)
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    active = models.BooleanField(verbose_name='Активен', default=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'API ключ'
        verbose_name_plural = 'API ключи'
        db_table = 'api_key'