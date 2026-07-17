from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст статті")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
        ordering = ['-created_at']  # Спочатку новіші

    def __str__(self):
        return self.title