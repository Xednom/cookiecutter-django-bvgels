from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, filters, generics
from djoser.email import ConfirmationEmail, PasswordResetEmail


User = get_user_model()


class ConfirmationEmail(ConfirmationEmail):
    template_name = "email/confirmation_email.html"


class PasswordResetEmail(PasswordResetEmail):
    template_name = "email/forgot_password_email.html"
