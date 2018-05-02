from django.conf.urls import include, url
from rest_framework import routers

from . import viewsets

ROUTER = routers.DefaultRouter()
ROUTER.register(r'posts', viewsets.PostViewSet)

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
]
