
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название отеля")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=200, verbose_name="Местоположение")
    rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Рейтинг")
    image = models.ImageField(upload_to='hotels/', blank=True, null=True, verbose_name="Изображение отеля")

    def __str__(self):
        return self.name
