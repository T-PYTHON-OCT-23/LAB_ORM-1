from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blogs
# Create your views here.

def add_blogs_views(request:HttpRequest):

    if request.method == 'POST':
        new_blogs = Blogs(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'])
        new_blogs.save()
        
        return redirect('blogs:show_blogs_views')
    
    return render(request, 'blogs/add_blogs.html')

def show_blogs_views(request:HttpRequest):
    blogs = Blogs.objects.all()

    return render(request, 'blogs/show_blogs.html',{'blogs':blogs})