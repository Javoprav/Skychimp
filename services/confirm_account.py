from django.conf import settings
from django.core.mail import send_mail


def confirm_account(obj):
    send_mail(
        subject='Подтверждение почты',
        message=f'Для подтверждения регистрации перейдите по ссылке: http://localhost:8000/users/activate/{obj.token}/',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[obj.email],
        fail_silently=False
    )
