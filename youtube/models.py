from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False) #todo: auto_now=True
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #Just trying upload to cloudnary.
    videoStorage = CloudinaryField("video")

class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

