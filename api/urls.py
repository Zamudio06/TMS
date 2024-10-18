from django.conf.urls import include, url
from rest_framework import routers

from api.viewsets import TaskViewset

router = routers.DefaultRouter()

router.register(r"task", TaskViewset)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"", include(router.urls)),
    url(r"api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
