from django.db import models

# Create your models here.
class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    phone = models.CharField(max_length=14)
    content = models.TextField()

    def __str__(self):
        return self.name