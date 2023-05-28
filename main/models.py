from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='почта')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=254, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Sending(models.Model):
    FREQUENCY_CHOICES = [
        ('1 раз в день', '1 раз в день'),
        ('1 раз в неделю', '1 раз в неделю'),
        ('1 раз в месяц', '1 раз в месяц'),
    ]

    SELECT_STATUS = [
        ('создана', 'Создана'),
        ('завершена', 'Завершена'),
        ('запущена', 'Запущена'),
    ]

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.TimeField()
    frequency = models.CharField(max_length=14, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, default='created', choices=SELECT_STATUS, verbose_name='Статус')

    def __str__(self):
        return self.message.subject

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Attempt(models.Model):
    STATUS_CHOICES = [
        ('в процессе', 'В процессе'),
        ('успешно', 'Успешно'),
        ('не удачно', 'Не удачно'),
    ]

    sending = models.ForeignKey(Sending, on_delete=models.CASCADE, verbose_name='Рассылка')
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус')
    response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return f"{self.sending.message.subject} - {self.sent_at}"

    class Meta:
        verbose_name = 'Статистика (попытка)'
        verbose_name_plural = 'Статистики (попытки)'