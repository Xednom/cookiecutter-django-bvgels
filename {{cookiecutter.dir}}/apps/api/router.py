from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()


app_name = "api"

urlpatterns = [path("v1/", include(router.urls), name="api")]
