from django.db import models


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def valid(self):
        return self.get_queryset().filter(valid=True)

    def in_valid(self):
        return self.get_queryset().filter(valid=False)


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    valid = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.title

