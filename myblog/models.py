from django.db import models

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