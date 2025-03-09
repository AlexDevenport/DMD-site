from django.db import models
from django import forms
from django.contrib.auth.models import User

# Персонаж
class Character(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя персонажа")
    additional_info = models.TextField(verbose_name="Прочая информация")
    photo_url = models.CharField(max_length=500, null=True, blank=True, verbose_name="Ссылка на фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

# Пользователь
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']