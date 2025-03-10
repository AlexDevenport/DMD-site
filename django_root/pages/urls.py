from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('main/', views.main_page, name='main'), # Главная страница
    path('form/', views.form_page, name='form'),  # Страница с формой
    path('navbar/', views.navbar, name='navbar'), # Навбар
    path('register/', views.register_page, name='register'), # Регистрация
    path('login/', views.login_view, name='login'), # Авторизация
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Выход
    path('char_list/', views.char_list_page, name='char_list'), # Список персонажей
    path('char_list_elem/', views.char_list_elem, name='char_list_elem'), # Элемент списка (персонаж)
]