from django.db import models

from main.models import NULLABLE
from users.models import User


class Post(models.Model):

    title = models.CharField(max_length=255, unique=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, blank=True, verbose_name='URL')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(verbose_name='Опубликован', default=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_by = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, related_name='post')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
