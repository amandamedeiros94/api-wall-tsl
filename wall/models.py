from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.message
