from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features', views.feature, name='feature'),
    path('post/<str:pk>', views.post, name='post'),
]