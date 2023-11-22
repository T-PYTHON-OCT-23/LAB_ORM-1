# blog/views.py
from django.shortcuts import render, redirect , get_object_or_404
from django.http import Http404
from .models import Post
from django.utils import timezone 
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.is_published = True
            post.published_at = timezone.now()  
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


def view_post(request, post_id):
    #post = Post.objects.get(id=post_id)
    post=get_object_or_404(Post, id=post_id)
    return render(request, 'blog/view_post.html', {'post': post})
    #raise Http404("Post does not exist")
    
    
    