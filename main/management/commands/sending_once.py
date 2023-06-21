from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from main.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        all_email = []
        for customer in Customer.objects.all():
            all_email.append(str(customer.email))

        for send in Sending.objects.all():
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
                status_list = []
                server_response = {
                    'sending': Sending.objects.get(pk=send.id),
                    # 'sent_at': datetime.datetime.now(),
                    'status': Attempt.DELIVERED,
                    'response': [*all_email]}
                status_list.append(Attempt(**server_response))
                Attempt.objects.bulk_create(status_list)
                # создание рассылки по Sending.frequency
                if send.frequency == Sending.ONCE:
                    send.status = Sending.COMPLETED
                    send.save()
                else:
                    send.status = Sending.LAUNCHED
                    send.save()
