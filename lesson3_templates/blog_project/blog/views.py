from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """Отримує всі пости та рендерить сторінку зі списком"""
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    """Отримує один пост за первинним ключем (pk) та рендерить детальну сторінку"""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})