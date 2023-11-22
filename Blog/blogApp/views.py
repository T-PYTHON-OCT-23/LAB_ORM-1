from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import Blog
from django.utils import timezone

# Create your views here.


def add_post_view(request: HttpRequest):

    if request.method == "POST":
        read_blog_item = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"],published_at=request.POST["published_at"])
        read_blog_item.save()

        return redirect("blogApp:read_blog_view")

    return render(request, "blogApp/add_post.html")




def read_blog_view(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "blogApp/read_blog.html", {"blogs" : blogs})

# handle with not found pages 
try:
    def detail_blog_view(request:HttpRequest , blog_id):

        blog = Blog.objects.get(id=blog_id)

        return render(request , "blogApp/detail.html" , {"blog":blog})
except Exception as e:
    print(e)

try:
    def update_view(request :HttpRequest , blog_id):
        blog=Blog.objects.get(id=blog_id)
        if request.method == "POST":
            updated_post = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"] , published_at=request.POST["published_at"])
            updated_post.save()

            return redirect("blogApp:read_blog_view" , blog_id=blog.id)
        return render(request ,"blogApp/update.html" ,  {"blog":blog})
except Exception as e:
    print(e)


try:
    def delete_view(request :HttpRequest , blog_id):
        blog=Blog.objects.get(id = blog_id)
        blog.delete()
        return redirect("blogApp:read_blog_view")
except Exception as e:
    print(e)