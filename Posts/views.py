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

def search(request):
    search = request.GET['search']
    if len(search) > 50:
        posts = []
    else:
        posts = Post.objects.filter(title__icontains=search)
    context = {
        'posts': posts,
        'search': search
    }
    return render(request, 'search.html', context)