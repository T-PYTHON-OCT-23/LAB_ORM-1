from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Published
# Create your views here.

def add_blog(request:HttpRequest):

    if request.method == 'POST':
        new_published = Published(title=request.POST['title'],content =request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'])
        new_published.save()
        return redirect(request,'blog_op:publications')

    return render (request,'blog_op/add.html')

def publications(request:HttpRequest):
    pub = Published.objects.all()

    return render(request,'blog_op/publications.html',{'publications':pub})