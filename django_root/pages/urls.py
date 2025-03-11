from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', views.main_page, name='main'), # Главная страница
    path('navbar/', views.navbar, name='navbar'), # Навбар
    path('register/', views.register_view, name='register'), # Регистрация
    path('login/', views.login_view, name='login'), # Авторизация
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Выход
    path('char_list/', views.char_list_page, name='char_list'), # Список персонажей
    path('char_list_elem/', views.char_list_elem, name='char_list_elem'), # Элемент списка (персонаж)
    path('form/', views.create_character, name='form'), # Создание персонажа
    path('sheet/<int:character_id>/', views.sheet_page, name='sheet'), # Редактирование персонажа
    path('delete_character/<int:character_id>/', views.delete_character, name='delete_character'), # Удаление персонажа
    path('check_character_name/', views.check_character_name, name='check_character_name'), # Проверка на уникальность персонажа
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
