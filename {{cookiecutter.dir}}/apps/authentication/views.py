from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, filters, generics

User = get_user_model()


# class CallMeConfirmationEmail(ConfirmationEmail):
#     template_name = "email/confirmation_email.html"


# class CallMePasswordResetEmail(PasswordResetEmail):
#     template_name = "email/forgot_password_email.html"
