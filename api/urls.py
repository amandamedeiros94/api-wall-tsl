from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from wall import urls as wall_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(wall_urls)),
]
