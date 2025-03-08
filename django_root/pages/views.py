from django.shortcuts import render
from .models import Character

# Create your views here.
def base(request):
    return render(request, 'pages/base.html')

def navbar(request):
    return render(request, 'pages/navbar.html')

def form_page(request):
    return render(request, 'pages/form.html')

def register_page(request):
    return render(request, 'pages/register.html')

def login_page(request):
    return render(request, 'pages/login.html')

def char_list_page(request):
    characters = Character.objects.all()  # Получаем всех персонажей из базы данных
    return render(request, 'pages/char_list.html', {'characters': characters})

def char_list_elem(request):
    return render(request, 'pages/char_list_elem.html')

def main_page(request):
    return render(request, 'pages/main.html')