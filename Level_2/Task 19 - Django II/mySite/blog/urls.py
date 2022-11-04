from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post
# url patterns from notes I just modified the template_name 
# because I placed my templates in a different folder
urlpatterns = [
    path('', ListView.as_view(queryset= Post.objects.all().order_by("-date")[:25],template_name="blog/blog.html")),   
    path('<int:pk>/',DetailView.as_view(model=Post, template_name="blog/post.html")),   
]