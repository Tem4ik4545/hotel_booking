from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating')  # Отображаемые поля в списке
    search_fields = ('name', 'location')  # Поля для поиска
