from django.db import models


class Post(models.Model):
    message = models.TextField()
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.message
