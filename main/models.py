from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()
    when = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{} at {}'.format(self.header, self.when)

    def number_of_comments(self):
        return self.comment_set.all().count()


class Comment(models.Model):
    post = models.ForeignKey('Post')
    text = models.TextField(u'Comment text')
    when = models.DateTimeField(auto_now=True)
    who = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u'Comment to "{}"'.format(self.post.header)