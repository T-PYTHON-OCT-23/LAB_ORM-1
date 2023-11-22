from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.
def add_blog_view(request: HttpRequest):

    #Creating a new entry into the database for a movie

    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"])
        try:
            new_blog.save()
        except Exception as e:
            return render(request,"blogs/not_exist.html")
            
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


def update_blog_view(request: HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Exception as e:
        return render(request,"blogs/not_exist.html")

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.published_at = request.POST["published_at"]
        blog.save()

        return redirect('blogs:blogs_details_view', blog_id=blog.id)
    
    return render(request, "blogs/update_blog.html", {"blog" : blog})


    
def delete_blog_view(request:HttpRequest,blog_id):
    blog= Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blogs:blogs_home_view")

