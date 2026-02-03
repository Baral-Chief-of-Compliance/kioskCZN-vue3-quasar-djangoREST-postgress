from django.db import models


class Version(models.Model):
    """Версия проекта"""
    major = models.PositiveIntegerField(verbose_name='Ломающие изменения, несовместимые с предыдущей версией', default=1)
    minor = models.PositiveBigIntegerField(verbose_name='Новые возможности, обратно совместимые', default=0)
    patch = models.PositiveIntegerField(verbose_name='Багфиксы, мелкие исправления', default=0)
    datetime = models.DateTimeField(verbose_name='Дата версии', auto_now=True)
    dev = models.BooleanField(verbose_name='Версия в разработке', default=False)
    alpha = models.BooleanField(verbose_name='Первая тестируемая сборка', default=False)
    beta = models.BooleanField(verbose_name='Стабильнее альфы. Основной функционал реализован', default=False)


    def __str__(self) -> str:
        version = '{}.{}.{}'.format(
            self.major,
            self.minor,
            self.patch
        )

        if self.dev:
            version += '-dev'
        elif self.alpha:
            version += '-alpha'
        elif self.beta:
            version += '-beta'

        return version
    
    class Meta:
        verbose_name = 'Версия проекта'
        verbose_name_plural = 'Версия проекта'
