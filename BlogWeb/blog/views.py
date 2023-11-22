from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
from django.utils import timezone
# Create your views here.



def add_blog_views(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"],  is_published=request.POST["is_published"], published_at=timezone.now())
        new_blog.save()
        return redirect("blog:home_blog_views")

    return render(request, "blog/add_blog.html")



def home_blog_views(request: HttpRequest):
     
    blog = Blog.objects.all()

    return render(request, "blog/home_blog.html", {"blog":blog})

def details_blog_views(request: HttpRequest,blog_id):
        try:
            blogs=Blog.objects.get(id=blog_id)
           
        except:
            return render(request, "blog/page_not_found.html")
         
        return render(request,"blog/details_blog.html",{"blogs":blogs})
             


