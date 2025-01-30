from django.db import models


class Post(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
    )
    description = models.TextField(
        verbose_name="Содержание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="posts/",
        verbose_name="Превью",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        editable=False,
    )
    was_publication = models.BooleanField(
        default=True,
        verbose_name="Опубликован пост",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["description", "name"]

    def __str__(self):
        return self.name
