from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.
def add_blog_view(request: HttpRequest):

    #Creating a new entry into the database for a movie

    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"])
        new_blog.save()

        return redirect("blogs:blogs_home_view")

    return render(request, "blogs/add.html")



def blogs_home_view(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "Blogs/blogs_home.html", {"blogs" : blogs})

def blogs_details_view(request:HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Exception as e:
        return render(request,"blogs/not_exist.html")
    return render(request , "blogs/blogs_details.html", {"blog":blog})

def not_exist(request:HttpRequest):
    return render(request,"blogs/not_exist.html")