from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

class Authored(models.Model):
    author = models.ForeignKey(User)
    class Meta:
        abstract = True

class Content(Authored):
    text = models.TextField()
    time = models.DateTimeField()
    class Meta:
        abstract = True

class FriendshipRequest(Authored):
    confirmed = models.BooleanField(null=False, default=False)
    goal = models.ForeignKey(User, related_name='goals')

class FriendShip(models.Model):
    first = models.ForeignKey(User, related_name='first')
    second = models.ForeignKey(User, related_name='second')

