from __future__ import unicode_literals

from django.db import models

from core.models import Authored, User, Content


class Chat(Authored):
    name = models.CharField(max_length=255, null=False)

class ChatMember(models.Model):
    chat = models.ForeignKey(Chat)
    user = models.ForeignKey(User)

class Message(Content):
    chat = models.ForeignKey(Chat)


# Create your models here.
