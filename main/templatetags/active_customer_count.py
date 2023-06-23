from django import template
from main.models import Customer
register = template.Library()


@register.simple_tag
def active_customer_count():
    count = Customer.objects.filter(is_active=True).count()
    return f'{count}'
