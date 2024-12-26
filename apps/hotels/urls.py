from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),  # Главная страница отелей
    path('<int:pk>/', views.hotel_detail, name='hotel_detail'),
]
