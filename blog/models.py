from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Blog_post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title =models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    body = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now)
    updated_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title  #set main field to be shown
    
class Blog_Image(models.Model):
    post = models.ForeignKey(Blog_post, on_delete=models.PROTECT)
    content_image = models.ImageField(upload_to='post_content_images/', blank=True)
    