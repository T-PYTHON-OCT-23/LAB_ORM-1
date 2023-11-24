from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
from django.utils import timezone
# Create your views here.


def add_blog_view(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=timezone.now(),category=request.POST["category"],poster=request.FILES["poster"])
        new_blog.save()

        return redirect("post:display_blog_view")

    return render(request, "post/add_post.html" , {"categories" : Blog.categories})


def display_blog_view(request: HttpRequest):

     posts = Blog.objects.all()

     return render(request, "post/display_blog.html", {"posts": posts})


def post_detail_view(request:HttpRequest, post_id):
 
    try:
      post=Blog.objects.get(id=post_id )

    except Exception as e:
        return render(request, "post/not_exist.html.")
        
    return render(request, "post/post_detail.html", {"post" : post})



def not_exist_view(request:HttpRequest):

   return render(request, "post/not_exist.html.")



def update_post_view(request: HttpRequest, post_id):

    post = Blog.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content= request.POST["content"]
        post.is_published = request.POST["is_published"]
        post.published_at = request.POST["published_at"]
        post.category = request.POST["category"]
        post.save()

        return redirect('post:post_detail_view', post_id=post.id)

    return render(request, "post/update.html", {"post" : post , "categories"  : Blog.categories})

 
def delete_post_view(request: HttpRequest, post_id):

    post = Blog.objects.get(id=post_id)
    post.delete()

    return redirect("post:display_blog_view")