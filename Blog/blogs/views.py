from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
# Create your views here.
def read(request : HttpRequest):
    blogs=Blog.objects.all()
    return render(request, "Blog/read.html", {"blogs" : blogs})

def add(request : HttpRequest):
    if request.method=="POST":
        new_blog=Blog(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'])
        new_blog.save()
        return redirect("Blog:read_blog")
    return render(request,'Blog/add.html')