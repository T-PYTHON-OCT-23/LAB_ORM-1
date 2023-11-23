from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
# Create your views here.
def read(request : HttpRequest, blog_id):
    blogs=Blog.objects.get(id=blog_id)
    return render(request, "Blogs/read.html", {"blogs" : blogs})

def add(request : HttpRequest):
    if request.method=="POST":
        new_blog=Blog(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'])
        new_blog.save()
        return redirect("blogs:read")
    return render(request,'blogs/add.html')


def detail(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    return render(request, "blogs/detail.html", {"blog" : blog})


def update(request: HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published "]
        blog.published_at= request.POST["published_at"]
        blog.save()

        return redirect('blogs:detail', blog_id=blog.id)

    return render(request, "blogs/update.html", {"blog" : blog})


def delete(request: HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blogs:home_blog")