from django.db import models


class Post(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок поста",
    )
    description = models.TextField(
        verbose_name="Содержание",
        help_text="Введите содержание поста",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="posts/",
        verbose_name="Превью",
        help_text="Вставьте изображение для поста",
        blank=True,
        null=True,
    )
    is_public = models.BooleanField(
        default=True,
        verbose_name="Признак публикации",
        help_text="Укажите, доступен ли пост для просмотра",
    )
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Количество просмотров поста",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания поста",
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        help_text="Дата и время последнего обновления поста",
        editable=False,
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["name"]

    def __str__(self):
        return self.name
