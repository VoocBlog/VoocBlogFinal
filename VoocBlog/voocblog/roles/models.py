from django.db import models
from django.utils import timezone
from django.conf import settings

import datetime
# Create your models here.
class Category(models.Model):
    topic = models.TextField()
    
    def __str__(self):
        return self.topic

class Post(models.Model):
    title_post = models.CharField(max_length=200)
    pub_date_post = models.DateTimeField(auto_now_add=True)
    body_post = models.TextField()
    image_post = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title_post
    def was_published_recently(self):
        return self.pub_date_post >= timezone.now() - datetime.timedelta(days=1)
        
class Interaction(models.Model):   
    content_cmt = models.TextField()
    date_cmt = models.DateTimeField(auto_now_add=True)
    is_like = models.IntegerField(default=0)
    like_amount = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content_cmt