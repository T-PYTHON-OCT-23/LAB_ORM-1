from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.

def add_blog_view(request: HttpRequest):
    #Creating a new entry into the database for a movie

    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"])
        new_blog.save()

        return redirect("blog:read_blog_view")

    return render(request, "blog/addBlog.html")


def read_blog_view(request: HttpRequest):

    blog = Blog.objects.all()

    return render(request, "blog/blog.html", {"blog" : blog})