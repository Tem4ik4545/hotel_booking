from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:  # Проверка, если пользователь суперпользователь
                login(request, user)
                return redirect('/admin/')  # Перенаправление на админку
            else:
                login(request, user)
                return redirect('hotels:hotel_list')  # Перенаправление на список отелей
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'accounts/login.html')


User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Пароли не совпадают.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Регистрация успешна! Теперь вы можете войти в систему.')
            return redirect('accounts:login_view')  # Перенаправление на страницу входа

    return render(request, 'accounts/register.html')



def logout_view(request):
    logout(request)
    return redirect('accounts:login_view')  # Перенаправление на страницу входа

