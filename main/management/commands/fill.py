from django.core.management import BaseCommand
from main.services import send_email
from main.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_email(Sending.ONCE)
