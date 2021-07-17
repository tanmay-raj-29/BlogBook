from django.db import models
from datetime import datetime
from .helpers import *
from froala_editor.fields import FroalaField

# Create your models here.
class Post(models.Model):
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