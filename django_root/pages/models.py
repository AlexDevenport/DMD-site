from django.db import models
from django import forms
from django.contrib.auth.models import User

# Персонаж
class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Имя персонажа")
    race = models.CharField(max_length=100, verbose_name="Раса")
    level = models.IntegerField(verbose_name="Уровень", default=1)
    character_class = models.CharField(max_length=100, verbose_name="Класс", blank=True, null=True)
    strength = models.IntegerField(verbose_name="СИЛ", default=1)
    dexterity = models.IntegerField(verbose_name="ЛОВ", default=1)
    constitution = models.IntegerField(verbose_name="ТЕЛ", default=1)
    intelligence = models.IntegerField(verbose_name="ИНТ", default=1)
    wisdom = models.IntegerField(verbose_name="МДР", default=1)
    charisma = models.IntegerField(verbose_name="ХАР", default=1)
    items = models.TextField(verbose_name="Предметы", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
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