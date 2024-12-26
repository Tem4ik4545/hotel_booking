from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_number', 'room_type', 'price', 'is_available')
    search_fields = ('hotel__name', 'room_number', 'room_type')
    list_filter = ('hotel', 'is_available')
