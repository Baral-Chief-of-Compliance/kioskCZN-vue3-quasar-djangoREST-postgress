from django.db import models

from .glossary import TITEL_NAME

class PCParentOrganization(models.Model):
    """Вышестоящая организация"""

    name = models.CharField(verbose_name=TITEL_NAME, max_length=512)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Вышестоящая организация'
        verbose_name_plural = 'Вышестоящие организации'


class PCParentOrganizationPhone(models.Model):
    """Телефон вышестоящий организации"""

    org = models.ForeignKey(verbose_name='Вышестоящая организация', to=PCParentOrganization, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=128)

    def __str__(self) -> str:
        return f'Номер "{self.org}"'
    
    class Meta:
        verbose_name = 'Номер телефона вышестоящей организации'
        verbose_name_plural = 'Номера телефонов вышестоящих организаций'
