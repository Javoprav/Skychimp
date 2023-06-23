from django import template
from django.core.mail import send_mail
from django.conf import settings
from main.models import *
register = template.Library()


def send_email(*args):
    all_email = []
    for customer in Customer.objects.all():
        all_email.append(str(customer.email))

    for send in Sending.objects.all():
        if send.status == Sending.CREATED and send.frequency == (str(*args)):
            message_for_filter = send.message
            message = Message.objects.filter(subject=message_for_filter)
            for mes in message:
                send_mail(
                    subject=mes.subject,
                    message=mes.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*all_email],
                )
                status_list = []
                server_response = {
                    'sending': Sending.objects.get(pk=send.id),
                    'status': Attempt.DELIVERED,
                    'response': [*all_email]}
                status_list.append(Attempt(**server_response))
                Attempt.objects.bulk_create(status_list)
                if send.frequency == Sending.ONCE:
                    send.status = Sending.COMPLETED
                    send.save()
                else:
                    send.status = Sending.LAUNCHED
                    send.save()


