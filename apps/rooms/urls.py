from django.urls import path
from . import views

urlpatterns = [
    path('<int:hotel_id>/', views.room_list, name='room_list'),
    path('', views.room_list, name='room_list'),  # Список комнат
    path('<int:room_id>/', views.room_detail, name='room_detail'),  # Детали комнаты
]
