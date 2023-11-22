from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Published
# Create your views here.

def add_blog(request:HttpRequest):
    
    if request.method == 'POST':
        
        try:
            new_published = Published(title=request.POST['title'],content =request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'])
            
            new_published.save()
        except Exception:
            return redirect('blog_op:add_blog')
    
        return redirect('blog_op:publications')

    return render (request,'blog_op/add.html')

def publications(request:HttpRequest):
    pub = Published.objects.all()
    
    return render(request,'blog_op/publications.html',{'publications':pub})



def published_detail(request:HttpRequest,published_id):
    try:
        publidhed = Published.objects.get(id=published_id)
        return render(request,'blog_op/detail.html',{'puplidhed':publidhed})
    except  Exception:
        return redirect('blog_op:publications')


def update(request:HttpRequest,published_id):
    published = Published.objects.get(id=published_id)
    if request.method == 'POST':
        published.title = request.POST["title"]
        published.content =request.POST['content']
        published.published_at=request.POST['published_at']
        published.save()
        redirect('blog_op:publications')
        
    return render(request,'blog_op/update.html',{'update':published})



def delete_blog(request:HttpRequest,published_id):
    
    published = Published.objects.get(id=published_id)
    published.delete()
    
    return redirect('blog_op:publications')



