from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blogs
# Create your views here.

def add_blogs_views(request:HttpRequest):

    if request.method == 'POST':
        new_blogs = Blogs(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'],name_publisher=request.POST['name_publisher'],published_location=request.POST['published_location'])
        new_blogs.save()
        
        return redirect('blogs:show_blogs_views')
    
    return render(request, 'blogs/add_blogs.html')

def show_blogs_views(request:HttpRequest):
    blogs = Blogs.objects.all()

    return render(request, 'blogs/show_blogs.html',{'blogs':blogs})

def show_blogs_detils_view(request:HttpRequest,mo_id):
    try:
        movie = Blogs.objects.get(id=mo_id)
        return render(request, 'blogs/show_blogs_detlies.html',{'blogs':movie})
    except Exception as e:
        return redirect('blogs:show_blogs_views')

def update_blogs_views(request:HttpRequest,mo_id):

    if request.method == 'POST':
        blogs = Blogs.objects.get(id=mo_id)
        blogs.title = request.POST['title']
        blogs.name_publisher = request.POST['name_publisher']
        blogs.published_location = request.POST['published_location']
        blogs.content = request.POST['content']
        blogs.is_published = request.POST['is_published']
        blogs.published_at = request.POST['published_at']
        blogs.save()

    return redirect('blogs:show_blogs_detils_view',blogs.id)

def delete_blogs_views(request:HttpRequest,mo_id):
    blogs = Blogs.objects.get(id=mo_id)
    blogs.delete()
    blogs.save()
    
    return redirect('blogs:show_blogs_views')