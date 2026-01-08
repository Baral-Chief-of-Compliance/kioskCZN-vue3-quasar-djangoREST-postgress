from django.db import models


class Post(models.Model):
    """Должность сотрудника КЦ"""
    p_name = models.CharField(verbose_name='Наименование должности')
    p_priority = models.PositiveIntegerField(verbose_name='Порядок отображения', default=999)

    def __str__(self) -> str:
        return self.p_name
    
    class Meta:
        verbose_name = 'Должность КЦ'
        verbose_name_plural = 'Должности КЦ'