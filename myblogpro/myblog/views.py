from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import blog

# Create your views here.



def add_blog_view(request: HttpRequest):

    #Creating a new entry into the database for a movie

    if request.method == "POST":
        new_blog = blog(name=request.POST["name"], plot=request.POST["plot"], rating=request.POST["rating"], release_date=request.POST["release_date"])
        new_blog.save()

        return redirect("myblog:blog_home_view")

    return render(request, "myblog/add.html")



def blog_home_view(request: HttpRequest):

    myblog = blog.objects.all()

    return render(request, "myblog/blog_home.html", {"myblog" : myblog})