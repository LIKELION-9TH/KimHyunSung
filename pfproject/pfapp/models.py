from django.db import models
from django.db.models.base import Model

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200)
    singer = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title