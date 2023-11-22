from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(is_published=True, published_at__lte=timezone.now()).order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True, published_at__lte=timezone.now())
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.is_published:
                post.published_at = timezone.now()
                return redirect('main:post_detail', pk=post.pk)
            post.save()
            return redirect('main:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})