from django.db import models


class PC(models.Model):
    """Кадровый центр"""
    pc_name = models.CharField(verbose_name="Наименование Кадрового центра", max_length=256)
    pc_url_path= models.CharField(verbose_name="Наименование url пути")
    pc_id_parsing = models.IntegerField(verbose_name="Id идентификации КЦ в телефонном справочнике")

    def __str__(self) -> str:
        return self.pc_name
    
    class Meta:
        verbose_name = 'Кадровый центр'
        verbose_name_plural = 'Кадровые центры'