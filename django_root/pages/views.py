from django.shortcuts import render, redirect
from .models import Character
import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
# from django.http import JsonResponse


# Create your views here.
def navbar(request):
    return render(request, 'pages/navbar.html')

@login_required
def char_list_page(request):
    # Фильтруем персонажей по текущему пользователю
    characters = Character.objects.filter(user=request.user)
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
        
        # Проверяем, что поля не пустые
        if not name or not race:
            messages.error(request, 'Пожалуйста, заполните все поля.')
            return redirect('form')  # Используем 'form'
        
        # Проверяем, существует ли уже персонаж с таким именем для текущего пользователя
        if Character.objects.filter(user=request.user, name=name).exists():
            messages.error(request, 'Персонаж с таким именем уже существует.')
            return redirect('form')  # Используем 'form'
        
        # Создание персонажа и привязка к текущему пользователю
        character = Character.objects.create(
            user=request.user,
            name=name,
            race=race,
        )
        messages.success(request, 'Персонаж успешно создан!')
        return redirect('sheet', character_id=character.id)

    return render(request, 'pages/form.html')


from django.core.files.storage import default_storage
from django.conf import settings
import uuid


@login_required
def sheet_page(request, character_id):
    character = get_object_or_404(Character, id=character_id)

    if request.method == 'POST':
        # Обновляем данные персонажа из формы
        character.name = request.POST.get('name')
        character.race = request.POST.get('race')
        character.level = request.POST.get('level')
        character.character_class = request.POST.get('character_class')
        character.strength = request.POST.get('strength')
        character.dexterity = request.POST.get('dexterity')
        character.constitution = request.POST.get('constitution')
        character.intelligence = request.POST.get('intelligence')
        character.wisdom = request.POST.get('wisdom')
        character.charisma = request.POST.get('charisma')
        character.items = request.POST.get('items')
        character.description = request.POST.get('description')

        # Обработка загруженной фотографии
        if 'photo_url' in request.FILES:
            photo = request.FILES['photo_url']
            # Генерируем уникальное имя файла
            file_extension = photo.name.split(".")[-1]
            unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
            file_path = os.path.join(settings.MEDIA_ROOT, unique_filename)

            # Сохраняем файл на сервере
            with default_storage.open(file_path, 'wb+') as destination:
                for chunk in photo.chunks():
                    destination.write(chunk)

            # Сохраняем путь к файлу в photo_url
            character.photo_url = os.path.join(settings.MEDIA_URL, unique_filename)

        character.save()

        # Перенаправляем на список персонажей
        return redirect('char_list')

    return render(request, 'pages/sheet.html', {'character': character})

@login_required
def delete_character(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    character.delete()
    return redirect('char_list')  # Перенаправляем на страницу списка персонажей

@login_required
def check_character_name(request):
    name = request.GET.get('name')
    exists = Character.objects.filter(user=request.user, name=name).exists()
    return JsonResponse({'exists': exists})