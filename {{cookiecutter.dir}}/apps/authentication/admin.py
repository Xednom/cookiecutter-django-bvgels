from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.authentication.models import (
    User,
)
from apps.authentication.resources import UserResource


User = get_user_model()


class UserProfileAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    list_filter = (
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
    )
    search_fields = (
        "first_name",
        "last_name",
        "username",
    )
    UserAdmin.fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Personal Informations"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, UserProfileAdmin)
