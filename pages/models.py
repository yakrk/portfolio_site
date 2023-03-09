from django.db import models
from datetime import datetime 

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.tag

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    card_image = models.ImageField()
    subtitle = models.CharField(max_length=200, blank=True)
    github_link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    feature_view_name = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag)
    def __str__(self) -> str:
        return self.title