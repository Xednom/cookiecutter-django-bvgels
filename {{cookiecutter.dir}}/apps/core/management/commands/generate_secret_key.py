from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = "Generate secret key"

    def handle(self, *args, **kwargs):
        self.style.SUCCESS(f"SECRET KEY: {get_random_secret_key()}")
