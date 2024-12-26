
from .models import Hotel
from .forms import HotelSearchForm
from apps.rooms.models import Room
from apps.bookings.models import Booking
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
def hotel_list(request):
    form = HotelSearchForm(request.GET or None)
    hotels = Hotel.objects.all()

    # Фильтры
    if form.is_valid():
        if form.cleaned_data['name']:
            hotels = hotels.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data['location']:
            hotels = hotels.filter(location__icontains=form.cleaned_data['location'])
        if form.cleaned_data['min_rating']:
            hotels = hotels.filter(rating__gte=form.cleaned_data['min_rating'])

    context = {
        'form': form,
        'hotels': hotels,
    }
    return render(request, 'hotels/hotel_list.html', context)





def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    room_type = request.GET.get('room_type')
    check_in_date = request.GET.get('check_in_date')
    check_out_date = request.GET.get('check_out_date')

    rooms = None  # Изначально пустой список комнат
    room_type_choices = Room.ROOM_TYPE_CHOICES

    # Если выбран только тип комнаты, возвращаем все комнаты этого типа
    if room_type and not (check_in_date and check_out_date):
        rooms = Room.objects.filter(hotel=hotel, room_type=room_type)
    # Если выбраны тип и даты, фильтруем по доступности
    elif room_type and check_in_date and check_out_date:
        rooms = Room.objects.filter(
            hotel=hotel,
            room_type=room_type,
            is_available=True
        ).exclude(
            bookings__check_in_date__lt=check_out_date,
            bookings__check_out_date__gt=check_in_date
        )

    # Собираем информацию о бронированиях для отображения в календаре
    room_bookings = {}
    if rooms:
        for room in rooms:
            bookings = Booking.objects.filter(room=room).values_list('check_in_date', 'check_out_date')
            room_bookings[room.id] = [
                {"start": booking[0].isoformat(), "end": booking[1].isoformat()} for booking in bookings
            ]

    context = {
        'hotel': hotel,
        'rooms': rooms,
        'room_type_choices': room_type_choices,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'room_bookings': room_bookings,
    }
    return render(request, 'hotels/hotel_detail.html', context)


