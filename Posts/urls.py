from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs', views.blogs, name='blogs'),
    path('features', views.feature, name='feature'),
    path('post/<str:slug>', views.post, name='post'),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('addblog', views.add_blog, name='addblog'),
]