from django.core.management import BaseCommand
from main.services import send_email


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_email()
