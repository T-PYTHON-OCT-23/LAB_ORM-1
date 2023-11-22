from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Blog
# Create your views here.


def add_blogs_view(request:HttpRequest):
    if request.method == "POST":
        new_blogs = Blog(title=request.POST["title"], content=request.POST["content"], is_published = request.POST["is_published"], published_at = request.POST["published_at"])
        new_blogs.save()
        return redirect("blogs:show_blogs_view")

    
    return render(request,"blogs/add.html")

def show_blogs_view(request:HttpRequest):
    
    blogs=Blog.objects.all()
    
    return render(request,"blogs/show_blogs.html", {"blogs" : blogs})