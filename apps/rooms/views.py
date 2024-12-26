
from .models import Room
from .forms import RoomSearchForm
from .forms import RoomForm
from django.shortcuts import render, get_object_or_404, redirect



def room_search(request):
    form = RoomSearchForm(request.GET or None)
    rooms = Room.objects.all()
    return render(request, 'rooms/room_search.html', {'form': form, 'rooms': rooms})

def room_list(request):
    """
    View to display the list of rooms with optional filtering.
    """
    rooms = Room.objects.all()

    # Apply filtering based on query parameters
    room_type = request.GET.get('room_type')
    if room_type:
        rooms = rooms.filter(room_type=room_type)

    context = {
        'rooms': rooms,
        'search_form': RoomSearchForm(request.GET)
    }

    return render(request, 'rooms/room_list.html', context)


def room_detail(request, room_id):
    """
    View to display the details of a specific room.
    """
    room = Room.objects.get(id=room_id)

    context = {
        'room': room
    }

    return render(request, 'rooms/room_detail.html', context)



