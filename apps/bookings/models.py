from django.conf import settings
from django.db import models
from apps.hotels.models import Hotel
from apps.rooms.models import Room
from django.core.validators import RegexValidator

class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Используем кастомную модель пользователя
        on_delete=models.CASCADE,
        related_name='bookings'

    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests = models.PositiveIntegerField()
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Введите корректный номер телефона.")],
        help_text="Формат: +123456789. До 15 цифр."
    )

    def __str__(self):
        return f"Booking {self.id} - {self.user} in Room {self.room.room_number}"
