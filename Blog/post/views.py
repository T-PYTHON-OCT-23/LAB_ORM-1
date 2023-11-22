from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Blog
from django.utils import timezone
# Create your views here.


def add_blog_view(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], Published_at=timezone.now())
        new_blog.save()
        return redirect("post:display_blog_view")


    return render(request, "post/add_post.html")


def display_blog_view(request: HttpRequest):

     posts = Blog.objects.all()

     return render(request, 'post/display_blog.html', {'posts': posts})



 
def post_detail_view(request:HttpRequest, post_id):

    post=get_object_or_404(Blog,id=post_id )


    return render(request, "post/post_detail.html", {"post" : post})
