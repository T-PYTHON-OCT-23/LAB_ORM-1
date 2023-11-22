from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone
import sqlite3

def add_blog_view(request: HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], is_publishd= True if "is_publishd" in request.POST else False, publishd_at=timezone.now())
        new_post.save()

        return redirect("posts:post_home_view")

    return render(request, "blog/add.html")



def post_home_view(request: HttpRequest):

    posts = Post.objects.all()

    return render(request, "blog/blog_home.html", {"posts" :posts})



def post_detail_view(request:HttpRequest, posts_id):
    try:
        posts = Post.objects.get(id=posts_id)
        return render(request, "blog/blog_detail.html", {"posts" : posts})
    except sqlite3.Error as er:
        print('SQLite error:404')




def update_post_view(request: HttpRequest, posts_id):

    posts = Post.objects.get(id=posts_id)

    if request.method == "POST":
        posts.title = request.POST["title"]
        posts.content = request.POST["content"]
        # Post.is_publishd = request.POST["is_publishd"]
        posts.publishd_at = request.POST["publishd_at"]
        posts.save()

        return redirect('posts:post_detail_view', posts_id=posts.id)

    return render(request, "blog/update.html", {"posts" : posts})


def delete_post_view(request: HttpRequest, posts_id):

    posts = Post.objects.get(id=posts_id)
    posts.delete()

    return redirect("posts:post_home_view")