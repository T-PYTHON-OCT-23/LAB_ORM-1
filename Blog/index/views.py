from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Sport
# Create your views here.

def add_view(request:HttpRequest):
    if request.method == "POST":
        sport=Sport(title= request.POST["title"],content=request.POST["content"],is_published=request.POST["is_published"],published_at=request.POST["published_at"] )
        sport.save()

        return redirect("index:home_view")
    return render (request,"index/add.html")

def home_view (request : HttpRequest):
    sport = Sport.objects.all()
    return render(request,"index/home.html",{'sport': sport})