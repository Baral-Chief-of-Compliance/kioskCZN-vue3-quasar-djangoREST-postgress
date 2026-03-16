from django.db import models

# Create your models here.
class Version(models.Model):
    major = models.PositiveIntegerField(
        verbose_name='major',
        help_text='Изменяется при несовместимых изменениях',
        default=0
    )
    minor = models.PositiveIntegerField(
        verbose_name='minor',
        help_text='Изменяется при совместимом добавлении функционала',
        default=0
    )
    patch = models.PositiveIntegerField(
        verbose_name='patch',
        help_text='Изменяется при совместимом исправлении ошибок',
        default=0
    )

    dev = models.BooleanField(
        verbose_name='Версия в разработке',
        help_text='Самая ранняя стадия, возможны ошибки.',
        default=False
    )

    alpha = models.BooleanField(
        verbose_name='Альфа-версия',
        help_text='Функционал функционален, но не тестирован до конца, содержит баги.',
        default=False
    )

    beta = models.BooleanField(
        verbose_name='Бета-версия',
        help_text='Протестирована, функционал заморожен, идет поиск мелких ошибок.',
        default=False
    )

    date = models.DateField(verbose_name='Дата', auto_now=True)

    def __str__(self):
        version = '{}.{}.{}'.format(
            self.major,
            self.minor,
            self.patch
        )

        version_type =''

        if self.dev:
            version_type = '-dev'
        
        elif self.alpha:
            version_type = '-alpha'
        
        elif self.patch:
            version_type = '-patch'
        
        version += '{} от {}'.format(version_type, self.date.strftime('%d.%m.%Y'))

        return version
    
    class Meta:
        verbose_name = 'Версия киоска'
        verbose_name_plural = 'Версия киоска'