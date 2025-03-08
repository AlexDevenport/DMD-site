from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),  # Главная страница
    path('form/', views.form_page, name='form'),  # Страница с формой
    path('navbar/', views.navbar, name='navbar'), # Навбар
]