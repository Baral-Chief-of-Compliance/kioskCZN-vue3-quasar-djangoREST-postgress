from django.db import models

from .glossary import TITEL_NAME, PC_PARENT_OGR

class PCParentOrganization(models.Model):
    """Вышестоящая организация"""

    name = models.CharField(verbose_name=TITEL_NAME, max_length=512)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = PC_PARENT_OGR
        verbose_name_plural = 'Вышестоящие организации'
        db_table = 'pc_parent_organization'


class PCParentOrganizationPhone(models.Model):
    """Телефон вышестоящий организации"""

    org = models.ForeignKey(verbose_name=PC_PARENT_OGR, to=PCParentOrganization, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=128)

    def __str__(self) -> str:
        return f'Номер "{self.org}"'
    
    class Meta:
        verbose_name = 'Номер телефона вышестоящей организации'
        verbose_name_plural = 'Номера телефонов вышестоящих организаций'
        db_table = 'pc_parent_organization_phone'


class PCParentOrganizationAddress(models.Model):
    """Адресс вышестоящий организации"""

    org = models.ForeignKey(verbose_name=PC_PARENT_OGR, to=PCParentOrganization, on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Адрес', max_length=256)

    def __str__(self) -> str:
        return f'Адрес "{self.org}"'
    
    class Meta:
        verbose_name = 'Адрес вышестоящий организации'
        verbose_name_plural = 'Адреса вышестоящих организаций'
        db_table = 'pc_parent_organization_address'


class PCParentOrganizationEmail(models.Model):
    """Электроный адрес вышестоящей организации"""

    org = models.ForeignKey(verbose_name=PC_PARENT_OGR, to=PCParentOrganization, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email')

    def __str__(self) -> str:
        return f'Email "{self.org}"'
    
    class Meta:
        verbose_name = 'Электроный адрес'
        verbose_name_plural = 'Элктронные адреса выщестоящих организаций'
        db_table = 'pc_parent_organization_email'
