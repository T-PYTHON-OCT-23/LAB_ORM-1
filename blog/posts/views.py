from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import posts

# Create your views here.



def add_blog_view(request: HttpRequest):

    #Creating a new entry into the database for a blog

    if request.method == "POST":
        new_post = posts(title=request.POST["title"], content=request.POST["content"], is_publishd=request.POST["is_publishd"], publishd_at=request.POST["publishd_at"])
        new_post.save()

        return redirect("posts:post_home_view")

    return render(request, "blog/add.html")



def post_home_view(request: HttpRequest):

    posts = posts.objects.all()

    return render(request, "blog/blog_home.html", {"posts" :posts})