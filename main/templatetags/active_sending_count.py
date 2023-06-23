from django import template
from main.models import Sending
register = template.Library()


@register.simple_tag
def active_sending_count():
    count = Sending.objects.filter(status=Sending.LAUNCHED).count()
    return f'{count} рассылки'
