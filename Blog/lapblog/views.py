from django.shortcuts import render ,redirect 
from .models import Web
from django.http import  HttpResponse ,HttpRequest
# Create your views here.
def add_blog_view(request: HttpRequest):

    #Creating a new entry into the database for a movie

    if request.method == "POST":
        new_Web = Web(Title =request.POST["Title"], Contant =request.POST["Contant"], is_published =request.POST["is_published"], published_at=request.POST["published_at"])
        new_Web.save()

        return redirect("lapblog:blog_home_view")

    return render(request, "lapblog/add.html")



def blog_home_view(request: HttpRequest):

    lapblog = Web.objects.all()

    return render(request, "lapblog/blog_home.html", {"lapblog" : lapblog})