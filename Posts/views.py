from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Feature
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

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
    if len(search) > 50 or len(search) == 0:
        posts = []
    else:
        posts = Post.objects.filter(title__icontains=search)
    context = {
        'posts': posts,
        'search': search
    }
    return render(request, 'search.html', context)

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if len(username) > 15:
            messages.error(request, 'Your username must be under 15 characters')
            return redirect('/')
        if password != password1:
            messages.error(request, 'passwords donot match')
            return redirect('/')            
        myUser = User.objects.create_user(username, email, password)
        myUser.save()
        login(request, myUser)
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials. Please try again')
            return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

def handlelogout(request):
    logout(request)
    return redirect('/')