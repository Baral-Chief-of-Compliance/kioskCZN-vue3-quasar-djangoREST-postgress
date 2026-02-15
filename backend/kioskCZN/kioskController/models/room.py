from django.db import models

from kioskController.models import Floor, PC
from .glossary import TITEL_NAME, DISPLAY_STATUS_NAME

class Room(models.Model):
    """Кабинет в кадровом центре"""

    floor = models.ForeignKey(
        verbose_name="Этаж кабинета", 
        to=Floor, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    pc = models.ForeignKey(
        verbose_name="Кадровый центр",
        to=PC,
        on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name=TITEL_NAME, max_length=128)
    vector_info = models.TextField(verbose_name="Векторная карта", blank=True, null=True)
    visible = models.BooleanField(verbose_name=DISPLAY_STATUS_NAME, blank=True, default=False)


    def __str__(self) -> str:
        return f'Кабинет "{self.name}" {self.pc}'
    
    class Meta:
        verbose_name = 'Комнаты КЦ'
        verbose_name_plural = 'Комнаты КЦ'
        db_table = 'room'