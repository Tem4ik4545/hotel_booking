from rest_framework import serializers
from apps.rooms.models import Room
from apps.bookings.models import Booking

class RoomSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'status', 'price']

class BookingSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'check_in', 'check_out']
