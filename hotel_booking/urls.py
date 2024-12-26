from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('accounts:login_view')),  # Перенаправление на авторизацию
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('hotels/', include('apps.hotels.urls', namespace='hotels')),
    path('bookings/', include('apps.bookings.urls', namespace='bookings')),
]
