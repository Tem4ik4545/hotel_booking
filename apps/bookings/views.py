from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from apps.rooms.models import Room
from apps.hotels.models import Hotel
from django.http import HttpResponseBadRequest
from datetime import datetime
@login_required
def booking_list(request):
    """
    Список всех бронирований текущего пользователя.
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def booking_create(request, room_id):
    # Получаем комнату по ID
    room = get_object_or_404(Room, pk=room_id)
    hotel = room.hotel  # Получаем отель из комнаты
    check_in_date = request.GET.get('check_in_date')
    check_out_date = request.GET.get('check_out_date')

    # Проверяем, что даты переданы
    if not check_in_date or not check_out_date:
        return HttpResponseBadRequest("Даты заезда и выезда обязательны.")

    # Преобразуем даты из строкового формата
    try:
        check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d").date()
        check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d").date()
    except ValueError:
        return HttpResponseBadRequest("Неверный формат даты. Ожидается формат YYYY-MM-DD.")

    # Проверяем, что дата выезда позже даты заезда
    if check_out_date <= check_in_date:
        return HttpResponseBadRequest("Дата выезда должна быть позже даты заезда.")

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Создаём бронирование, добавляя пользователя, комнату и отель
            booking = form.save(commit=False)
            booking.room = room
            booking.hotel = hotel  # Устанавливаем отель
            booking.user = request.user  # Добавляем текущего пользователя
            booking.check_in_date = check_in_date
            booking.check_out_date = check_out_date
            booking.save()
            return render(request, 'bookings/booking_success.html', {'booking': booking})
    else:
        # Предзаполняем форму
        form = BookingForm(initial={
            'check_in_date': check_in_date,
            'check_out_date': check_out_date
        })

    # Передаём данные в шаблон
    context = {
        'room': room,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'form': form,
    }
    return render(request, 'bookings/booking_form.html', context)


@login_required
def booking_detail(request, pk):
    """
    Детали конкретного бронирования по его первичному ключу (ID).
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

@login_required
def booking_update(request, pk):
    """
    Обновление информации о бронировании.
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Бронирование обновлено.')
            return redirect('bookings:booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form, 'booking': booking})

@login_required
def booking_delete(request, pk):
    """
    Удаление бронирования.
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Бронирование успешно удалено.')
        return redirect('bookings:booking_list')
    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})
