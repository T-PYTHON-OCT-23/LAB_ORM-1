from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.


def home(request: HttpRequest):
    return render(request, "main/home.html")


def add_blog(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(
            name=request.POST["name"], paragraph=request.POST["paragraph"], release_date=request.POST["release_date"])
        new_blog.save()

        return redirect("main:read_blog")

    return render(request, "main/add.html")


def read_blog(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "main/read.html", {"blogs": blogs})


def detail_blog(request: HttpRequest, blog_id):
    blogs = blog.objects.get(id=blog_id)
    return render(request, "main/detail.html", {"blogs": blogs})


def update_blog(request: HttpRequest, blog_id):
    blogs = blog.objects.get(id=blog_id)
    return render(request, "main/detail.html", {"blogs": blogs})


def delete_blog(request: HttpRequest, blog_id):
    blogs = blog.objects.get(id=blog_id)
    return render(request, "main/detail.html", {"blogs": blogs})
