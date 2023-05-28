from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='почта')
    message = models.TextField()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=254)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Sending(models.Model):
    FREQUENCY_CHOICES = [
        ('once', 'Once'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    SELECT_STATUS = [
        ('created', 'Created'),
        ('completed', 'Completed'),
        ('launched', 'Launched'),
    ]

    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.TimeField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    status = models.CharField(max_length=50, default='created', choices=SELECT_STATUS)

    def __str__(self):
        return self.message.subject


class Attempt(models.Model):
    STATUS_CHOICES = [
        ('in progress', 'In Progress'),
        ('success', 'Success'),
        ('failure', 'Failure'),
    ]

    broadcast = models.ForeignKey(Sending, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    response = models.TextField(**NULLABLE)

    def __str__(self):
        return f"{self.broadcast.message.subject} - {self.sent_at}"
