from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import viewsets

ROUTER = routers.DefaultRouter()
ROUTER.register(r'posts', viewsets.PostViewSet)
ROUTER.register(r'users', viewsets.UserViewSet)

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
    url(r'^obtain-auth-token/$', obtain_auth_token),
]
