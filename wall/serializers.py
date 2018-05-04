from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import serializers

from . import models


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'message', 'date', 'user')
        depth = 1


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'message', 'user')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        send_mail(
            'Welcome to the TSL Wall',
            'Thank you for registering at TSL Wall!\n\n'
            'You can post new messages on:\n'
            'http://web-wall-tsl.herokuapp.com\n\n'
            'Regards,\n'
            'Amanda.',
            'amandamedeiros.nave@gmail.com',
            [validated_data['email']],
            fail_silently=True
        )

        return user
