from django.shortcuts import render, redirect
from .models import Character

from django.contrib.auth import authenticate, login
from django.contrib import messages
# from django.contrib.auth.models import User


# Create your views here.
def navbar(request):
    return render(request, 'pages/navbar.html')

def form_page(request):
    return render(request, 'pages/form.html')

def register_page(request):
    return render(request, 'pages/register.html')

def char_list_page(request):
    characters = Character.objects.all()  # Получаем всех персонажей из базы данных
    return render(request, 'pages/char_list.html', {'characters': characters})

def char_list_elem(request):
    return render(request, 'pages/char_list_elem.html')

def main_page(request):
    return render(request, 'pages/main.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Получаем логин из формы
        password = request.POST.get('password')  # Получаем пароль из формы

        # Проверяем, совпадают ли данные с базой данных
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Если пользователь аутентифицирован, выполняем вход
            login(request, user)
            return redirect('main')  # Перенаправляем на главную страницу
        else:
            # Если данные неверные, показываем сообщение об ошибке
            messages.error(request, 'Неверный логин или пароль')
            return redirect('login')  # Возвращаем на страницу входа
    else:
        return render(request, 'pages/login.html')
