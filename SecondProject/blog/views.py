from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.

def add_blog_view(request: HttpRequest):
    #Creating a new entry into the database for a movie
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"],  category=request.POST["category"]  , content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"]  ,  poster=request.FILES["poster"])
        new_blog.save()

        return redirect("blog:read_blog_view")

    return render(request,"blog/addBlog.html", {"categories" : Blog.categories})


def read_blog_view(request: HttpRequest):

    blog = Blog.objects.all()

    return render(request, "blog/blog_home.html", {"blog" : blog})


def blog_detail_view(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    return render(request, "blog/blog_detail.html", {"blog" : blog})



def update_blog_view(request: HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.category = request.POST["category"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.published_at= request.POST["published_at"]
        blog.poster=request.POST["poster"]
        blog.save()

        return redirect('blog:blog_detail_view', blog_id=blog.id)

    return render(request, "blog/update.html", {"blog" : blog , "categories"  : Blog.categories})


def delete_blog_view(request: HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blog:read_blog_view")


#def find_page_view(request: HttpRequest, blog_id):
##  blog = Blog.objects.get(id=blog_id)
#  return redirect("blog:find_page_view", blog_id!=blog.id)
# return render( "blog/page_find.html")
