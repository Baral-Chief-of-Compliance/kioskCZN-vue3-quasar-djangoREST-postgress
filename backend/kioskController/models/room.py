from django.db import models

from kioskController.models.floor import Floor

class Room(models.Model):
    """Кабинет в кадровом центре"""

    r_floor = models.ForeignKey(verbose_name="Этаж кабинета", to=Floor, on_delete=models.CASCADE)
    r_name = models.CharField(verbose_name="Наименование кабинета", max_length=128)
    r_vector_info = models.TextField(verbose_name="Векторная карта", blank=True, null=True)


    def __str__(self) -> str:
        return f'Кабинет "{self.r_name}" {self.r_floor}'
    
    class Meta:
        verbose_name = 'Этаж КЦ'
        verbose_name_plural = 'Этажи КЦ'