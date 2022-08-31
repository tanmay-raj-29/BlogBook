from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .helpers import *
from froala_editor.fields import FroalaField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=100)
    body = FroalaField()
    institute = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(Post, self).save(*args, **kwargs)

class Feature(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)


class Comment(models.Model):
    post= models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    body= models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)