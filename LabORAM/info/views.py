from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Info

# Create your views here.



def add_info_view(request: HttpRequest):

    #Creating a new entry into the database for a movie

    if request.method == "POST":
        new_info = Info(title=request.POST["title"], contant=request.POST["contant"], is_published=request.POST["is_published"], published_at=request.POST["published_at"])
        new_info.save()

        return redirect("info:info_home_view")

    return render(request, "info/add.html")



def info_home_view(request: HttpRequest):

    info = Info.objects.all()
    
    return render(request, "info/info_home.html", {"info" : info})