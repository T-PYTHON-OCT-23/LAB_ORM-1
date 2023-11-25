from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

def add_blog_view(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"],category=request.POST["category"],image=request.FILES["image"])
        new_blog.save()

        return redirect("blogs:blogs_home_view")

    return render(request, "blogs/add.html", {"categories" : Blog.categories})



def blogs_home_view(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "Blogs/blogs_home.html", {"blogs" : blogs})


def blogs_details_view(request:HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    
    return render(request , "blogs/blogs_details.html", {"blog":blog})



def not_exist(request:HttpRequest):
    return render(request,"blogs/not_exist.html")


def update_blog_view(request: HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        if request.method == "POST":
            blog.title = request.POST["title"]
            blog.content = request.POST["content"]
            blog.is_published = request.POST["is_published"]
            blog.published_at = request.POST["published_at"]
            blog.category = request.POST["category"]
            blog.save()

            return redirect('blogs:blogs_details_view', blog_id=blog.id)
    except Exception as e:
        return render(request,"blogs/not_exist.html")


    return render(request, "blogs/update_blog.html", {"blog" : blog, "categories": Blog.categories})


    
def delete_blog_view(request:HttpRequest,blog_id):

    blog= Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blogs:blogs_home_view")


