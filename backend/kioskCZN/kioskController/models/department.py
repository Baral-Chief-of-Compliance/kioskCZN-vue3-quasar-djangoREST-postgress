from django.db import models

from .glossary import PC_NAME, DISPLAY_ORDER_NAME, DISPLAY_STATUS_NAME, TITEL_NAME
from kioskController.models import PC


class Department(models.Model):
    """Отдел кадрового центра"""

    pc = models.ForeignKey(verbose_name=PC_NAME, to=PC, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=TITEL_NAME, max_length=256)
    priority = models.PositiveIntegerField(verbose_name=DISPLAY_ORDER_NAME, default=999)
    visible = models.BooleanField(verbose_name=DISPLAY_STATUS_NAME, default=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Отдел кадрового центра'
        verbose_name_plural = 'Отделы кадровых центров'
        db_table = 'department'