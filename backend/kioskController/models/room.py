from django.db import models

from kioskController.models.floor import Floor
from .glossary import TITEL_NAME

class Room(models.Model):
    """Кабинет в кадровом центре"""

    floor = models.ForeignKey(verbose_name="Этаж кабинета", to=Floor, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=TITEL_NAME, max_length=128)
    vector_info = models.TextField(verbose_name="Векторная карта", blank=True, null=True)


    def __str__(self) -> str:
        return f'Кабинет "{self.name}" {self.floor}'
    
    class Meta:
        verbose_name = 'Этаж КЦ'
        verbose_name_plural = 'Этажи КЦ'