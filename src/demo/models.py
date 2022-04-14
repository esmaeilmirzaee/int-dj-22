from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


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


def post_model_post_save_receiver(sender, *args, **kwargs):
    print('This is the post save message.')


post_save.connect(post_model_post_save_receiver, sender=Post)


@receiver(post_delete)
def post_model_post_delete_receiver(sender, *args, **kwargs):
    print('This is the post delete message.')
