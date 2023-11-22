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