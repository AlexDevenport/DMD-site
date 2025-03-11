from django.shortcuts import render, redirect
from .models import Character

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
# from django.http import JsonResponse


# Create your views here.
def navbar(request):
    return render(request, 'pages/navbar.html')

def char_list_page(request):
    characters = Character.objects.all()  # Получаем всех персонажей из базы данных
    return render(request, 'pages/char_list.html', {'characters': characters})

def char_list_elem(request):
    return render(request, 'pages/char_list_elem.html')

def main_page(request):
    return render(request, 'pages/main.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверяем, что поля не пустые
        if not username or not password:
            messages.error(request, 'Пожалуйста, заполните все поля.')
            return redirect('login')

        # Проверяем, совпадают ли данные с базой данных
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Если пользователь аутентифицирован, выполняем вход
            login(request, user)
            return redirect('main')  # Перенаправляем на главную страницу
        else:
            # Если данные неверные, показываем сообщение об ошибке
            messages.error(request, 'Неверный логин или пароль')
            return redirect('login')  # Возвращаем на страницу авторизации
    else:
        return render(request, 'pages/login.html')
    
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Проверка на совпадение паролей
        if password1 != password2:
            messages.error(request, 'Пароли не совпадают.')
            return redirect('register')

        # Проверка на уникальность имени пользователя
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
            return redirect('register')

        # Создание нового пользователя
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Автоматический вход после регистрации
        login(request, user)
        messages.success(request, 'Регистрация прошла успешно!')
        return redirect('register')

    else:
        return render(request, 'pages/register.html')
    
@login_required
def create_character(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        race = request.POST.get('race')
        
        # Создание персонажа и привязка к текущему пользователю
        character = Character.objects.create(
            user=request.user,
            name=name,
            race=race,
        )
        return redirect('sheet', character_id=character.id)  # Передача ID персонажа

    return render(request, 'pages/form.html')

@login_required
def sheet_page(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'pages/sheet.html', {'character': character})