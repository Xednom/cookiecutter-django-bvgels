from django.db import models
from django.contrib.auth.models import AbstractUser

from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped

class User(AbstractUser):
    phone = models.CharField(blank=True, max_length=50)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone",
        "email",
    ]

    @property
    def user_full_name(self):
        return f"{self.first_name} {self.last_name}"
