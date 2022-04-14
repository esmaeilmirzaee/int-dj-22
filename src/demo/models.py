from django.db import models


class PostQuerySet(models.QuerySet):
    def valid(self):
        return self.filter(valid=True)

    def in_valid(self):
        return self.filter(valid=False)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(model=self.model, using=self._db)

    def valid(self):
        return self.get_queryset().valid()

    def in_valid(self):
        return self.get_queryset().in_valid()


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    valid = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.title

