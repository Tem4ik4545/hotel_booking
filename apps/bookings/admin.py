from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Проверьте правильность названий полей модели
    list_display = ('id', 'room', 'check_in_date', 'check_out_date', 'guests')  # Убедитесь, что эти поля есть в модели
    list_filter = ('room', 'check_in_date', 'check_out_date')  # Опционально: фильтры
    search_fields = ('room__room_number',)  # Поиск по номеру комнаты
