

# Create your models here.

from apps.hotels.models import Hotel
from django.db import models


class Room(models.Model):
    is_available = models.BooleanField(default=True)
    SINGLE = 'single'
    DOUBLE = 'double'
    SUITE = 'suite'
    ROOM_TYPE_CHOICES = [
        (SINGLE, 'Одноместная'),
        (DOUBLE, 'Двухместная'),
        (SUITE, 'Люкс'),
    ]
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10, unique=True, default="unknown")
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)  # True - свободен, False - забронирован
    max_guests = models.PositiveIntegerField(default=1, verbose_name="Максимальное количество гостей")
    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"


