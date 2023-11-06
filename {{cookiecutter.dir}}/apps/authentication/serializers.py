from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from django.contrib.auth import get_user_model
from .models import Client, Staff

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as BaseUserListSerializer

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone",
        )


class UserListSerializer(BaseUserListSerializer):
    class Meta(BaseUserListSerializer.Meta):
        fields = BaseUserListSerializer.Meta.fields + (
            "email",
            "phone",
        )
class CurrentUserSerializer(BaseUserListSerializer, WritableNestedModelSerializer):
    class Meta(BaseUserListSerializer.Meta):
        fields = BaseUserListSerializer.Meta.fields + (
            "phone",
            "first_name",
            "last_name",
            "is_superuser",
        )
