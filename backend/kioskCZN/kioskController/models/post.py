from django.db import models

from .glossary import DISPLAY_ORDER_NAME, TITEL_NAME

class Post(models.Model):
    """Должность сотрудника КЦ"""
    name = models.CharField(verbose_name=TITEL_NAME)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Должность КЦ'
        verbose_name_plural = 'Должности КЦ'
        db_table = 'post'