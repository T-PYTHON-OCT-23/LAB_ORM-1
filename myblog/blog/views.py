# blog/views.py
from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone 
from .forms import PostForm
def post_list(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.is_published = True
            post.published_at = timezone.now()  # Make sure to import timezone
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})
