from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.


def home(request: HttpRequest):
    return render(request, "main/home.html")


def add_blog(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(
            name=request.POST["name"], paragraph=request.POST["paragraph"], release_date=request.POST["release_date"], category = request.POST["category"] , image = request.FILES["image"])
        new_blog.save()

        return redirect("main:read_blog", {"categories" : Blog.categories})

    return render(request, "main/add.html")


def read_blog(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "main/read.html", {"blogs": blogs})


def detail_blog(request: HttpRequest, blog_id):
    blogs = Blog.objects.get(id=blog_id)
    return render(request, "main/detail.html", {"blog": blogs})


def update_blog(request: HttpRequest, blog_id):
        blogs = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.name = request.POST["name"]
        blog.paragraph = request.POST["paragraph"]
        blog.release_date = request.POST["release_date"]
        blog.category = request.POST["category"]
        blog.image = request.FILES["image"]
        blog.save()

        return redirect("main:read_blog", blog_id=blog.id)
    return render(request, "main/update.html", {"blogs": blogs},  {"categories" : Blog.categories})


def delete_blog(request: HttpRequest, blog_id):
    blogs = Blog.objects.get(id=blog_id)
    Blog.delete()
    return redirect("main:read_blog")
