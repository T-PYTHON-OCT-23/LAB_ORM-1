from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import blog

# Create your views here.



def add_blog_view(request: HttpRequest):

    #Creating a new entry into the database for a blog

    if request.method == "POST":
        new_blog = blogs(name=request.POST["name"], plot=request.POST["plot"], rating=request.POST["rating"], release_date=request.POST["release_date"])
        new_blog.save()

        return redirect("blog:blogs_home_view")

    return render(request, "blog/add.html")



def blogs_home_view(request: HttpRequest):

    blog = blog.objects.all()

    return render(request, "movies/movies_home.html", {"blog" : b})