from django.shortcuts import render
from apps.rooms.models import Room
from apps.bookings.models import Booking

def search(request):
    """
    Представление для обработки поиска.
    """
    query = request.GET.get('q', '')  # Получаем параметр запроса
    rooms = None
    bookings = None

    if query:
        # Фильтрация комнат по типу или номеру
        rooms = Room.objects.filter(room_type__icontains=query) | Room.objects.filter(room_number__icontains=query)

        # Фильтрация бронирований (например, по дате заезда/выезда или номеру комнаты)
        bookings = Booking.objects.filter(room__room_number__icontains=query)

    context = {
        'query': query,
        'rooms': rooms,
        'bookings': bookings,
    }
    return render(request, 'search/search.html', context)
