from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = "Generate secret key"

    def handle(self, *args, **kwargs):
        secret_key = get_random_secret_key()
        self.stdout.write(self.style.SUCCESS(f"{secret_key}"))
