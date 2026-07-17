from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post


def post_list(request):
    """Повертає список усіх статей у форматі JSON"""
    # Вибираємо лише необхідні поля з бази даних
    posts = Post.objects.all().values('id', 'title', 'content', 'created_at')

    # values() повертає QuerySet, тому перетворюємо його на звичайний список (list)
    posts_list = list(posts)

    # safe=False дозволяє передавати список (list) замість словника (dict) як кореневий елемент JSON
    # json_dumps_params={'ensure_ascii': False} запобігає екрануванню кирилиці (щоб текст залишався читабельним)
    return JsonResponse(posts_list, safe=False, json_dumps_params={'ensure_ascii': False})


def post_detail(request, pk):
    """Повертає детальну інформацію про один конкретний пост у форматі JSON"""
    post = get_object_or_404(Post, pk=pk)

    # Формуємо словник із даними об'єкта
    data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'created_at': post.created_at.isoformat()  # явно переводимо дату в ISO-формат для надійності
    }

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})