import uuid

from django.contrib.auth.models import User
from django.db import models


class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        abstract = True


class Board(Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300)


class Topic(Model):
    subject = models.CharField(max_length=300)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)


class Post(Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    update_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    update_by = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
