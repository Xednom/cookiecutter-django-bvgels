from django.db import models
from django.contrib.auth.models import AbstractUser


class StaffStatus(models.TextChoices):
    regular = "regular", ("Regular")
    probitionary = "probitionary", ("Probitionary")
    inactive = "inactive", ("Inactive")


class StaffCategory(models.TextChoices):
    office_based = "office_based", ("Office Based")
    part_timers = "part_timers", ("Part-timers")
    home_based = "home_based", ("Home Based")


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
