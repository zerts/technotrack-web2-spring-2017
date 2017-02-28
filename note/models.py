from __future__ import unicode_literals

from django.db import models

from core.models import Authored, Content
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Like(Authored):
    target_content_type = models.ForeignKey(ContentType)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_id')


class Likable(Content):
    likes = GenericRelation(Like, content_type_field='target_content_type', object_id_field='target_id', default=None)

    class Meta:
        abstract = True


class Post(Likable):

    def __unicode__(self):
        return 'Post #' + str(self.pk) + '_____author: ' + self.author.username + '______time: ' + str(self.time)



class Comment(Likable):
    post = models.ForeignKey(Post, related_name='post')

# Create your models here.


# Create your models here.
