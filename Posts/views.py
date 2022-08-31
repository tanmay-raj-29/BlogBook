from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import BlogForm, commentForm
from .models import Feature, Post

# Create your views here.

def index(request):
    post = Post.objects.last()
    context = {
        'post': post
    }
    return render(request, 'index.html', context)

def blogs(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blogs.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    model= commentForm
    
    if request.method=="POST":
        
        form= commentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form = form.save(commit=False)
            form.post_id = post.id
            form.save()
            return redirect('/blogs')
        else:
            return redirect('/')
    context = {
        'post': post,
        'model': model
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
        institutePosts = Post.objects.filter(institute__icontains=search)
        posts = posts.union(institutePosts)
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

def add_blog(request):
    # context = {}
    
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            # print(request.FILES)
            title = request.POST.get('title')
            institute = request.POST.get('institute')

            if form.is_valid():
                body = form.cleaned_data['body']

            blog_obj = Post.objects.create(
                title = title, 
                body = body,
                institute = institute,
            )
            return redirect('/blogs')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'addblog.html' , context)
