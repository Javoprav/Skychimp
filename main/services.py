from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from main.models import *


def send_email():  # отправка письма
    # sendings = Sending.objects.filter(status='Создана')
    all_email = []

    for customer in Customer.objects.all():
        all_email.append(str(customer.email))

    # print(all_email)
    for send in Sending.objects.all():
        if send.status == 'Создана':
            message1 = send.message
            message = Message.objects.filter(subject=message1)
            for mes in message:
                send_mail(
                    subject=mes.subject,
                    message=mes.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*all_email],
                )
            # создание статистики из модели Attempt

            # создание рассылки по Sending.frequency