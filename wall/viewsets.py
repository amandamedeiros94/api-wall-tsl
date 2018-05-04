from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all().order_by('-date')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PostListSerializer

        return serializers.PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserListSerializer

        return serializers.UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'validate-auth-token':
            return Response(
                serializers.UserListSerializer(
                    request.user,
                    context={'request': request}
                ).data
            )
        return super(UserViewSet, self).retrieve(request, pk)
