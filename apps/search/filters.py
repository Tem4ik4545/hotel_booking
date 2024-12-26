import django_filters
from apps.rooms.models import Room
from apps.bookings.models import Booking

class RoomFilter(django_filters.FilterSet):
    room_type = django_filters.CharFilter(field_name='room_type', lookup_expr='icontains')
    status = django_filters.BooleanFilter(field_name='status')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Room
        fields = ['room_type', 'status', 'price_min', 'price_max']


class BookingFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    room = django_filters.CharFilter(field_name='room__room_number', lookup_expr='icontains')
    check_in_after = django_filters.DateFilter(field_name='check_in', lookup_expr='gte')
    check_out_before = django_filters.DateFilter(field_name='check_out', lookup_expr='lte')

    class Meta:
        model = Booking
        fields = ['user', 'room', 'check_in_after', 'check_out_before']
