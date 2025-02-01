from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Почта пользователя",
        help_text="Введите электронную почту",
    )
    phone = models.CharField(
        max_length=11,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона пользователя",
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="Аватар пользователя",
        help_text="Загрузите изображение профиля",
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна проживания",
        help_text="Укажите страну проживания пользователя",
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
