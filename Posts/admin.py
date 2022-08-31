from django.contrib import admin

from .models import Comment, Feature, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Feature)
admin.site.register(Comment)
