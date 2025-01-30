from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="product/image",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Наименование категории",
        null=True,
        blank=True,
        related_name="category",
        on_delete=models.SET_NULL,
    )
    price = models.CharField(max_length=100, verbose_name="Цена")
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        auto_now=True,
        editable=False,
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        auto_now=True,
        editable=False,
    )
    was_publication = models.BooleanField(
        default=True,
        verbose_name="Опубликован ли"
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Владелец",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["description", "name"]
        permissions = [
            ("can_unpublish_product", "Может снять товар с публикации"),
            ("can_delete_product", "Может удалить товар"),
        ]

    def __str__(self):
        return self.name
