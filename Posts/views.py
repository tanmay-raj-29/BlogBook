from django.shortcuts import render
from .models import Post, Feature
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'post.html', context)

def feature(request):
    features = Feature.objects.all()
    context = {
        'features': features
    }
    return render(request, 'features.html', context)