from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='почта')
    message = models.TextField()

    def __str__(self):
        return f'{self.email} ({self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'