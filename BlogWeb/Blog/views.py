from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog1
# Create your views here.

def read_blog(request : HttpRequest):
    blogs=Blog1.objects.all()
    return render(request, "Blog/read_blog.html", {"blogs" : blogs})

def add_blog(request : HttpRequest):
    if request.method=="POST":
        new_blog=Blog1(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'])
        new_blog.save()
        return redirect("Blog:read_blog")
    return render(request,'Blog/add_blog.html')

def blog_detail(request : HttpRequest,blog_id):
    try:
        blog=Blog1.objects.get(id=blog_id)
    except Exception as e :
        return render(request,'Blog/not_exist.html')
    return render(request,'Blog/blog_detail.html',{'blog':blog})


def not_exist(request : HttpRequest):
    return render(request,'Blog/not_exist.html')