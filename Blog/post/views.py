from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
# Create your views here.


def add_blog_view(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], Published_at=request.POST["published_at"])
        new_blog.save()
        return redirect("post:display_blog_view")


    return render(request, "post/add_post.html")


def display_blog_view(request: HttpRequest):

     post = Blog.objects.all()

     return render(request, 'post/display_blog.html', {'posts': post})



 
