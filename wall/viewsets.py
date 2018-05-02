from rest_framework import viewsets

from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all().order_by('-date')
    serializer_class = serializers.PostSerializer
