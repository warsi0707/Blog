from django.db import models
from django.contrib.auth.models import User
from asyncio.windows_events import NULL
from pickle import TRUE
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author =models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    timestamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return "posted by " + self.author + ' - ' + self.title



class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment
    