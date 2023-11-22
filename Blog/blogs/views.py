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

def not_found_view(request:HttpRequest):
        return render(request,"blogs/not_found.html")

def blog_detail_view(request:HttpRequest, blog_id):
    
    try :
        blog = Blog.objects.get(id=blog_id)
        return render(request,"blogs/detail.html" , {"blog":blog})
    except Exception as e:
        return redirect("blogs:not_found_view")
