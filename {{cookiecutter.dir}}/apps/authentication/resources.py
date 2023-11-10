from import_export import resources
from apps.authentication.models import User, Client, Staff


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
        )
