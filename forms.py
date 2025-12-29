# Імпортуємо виняток PermissionDenied з Django,
# який використовується для заборони доступу (HTTP 403)
from django.core.exceptions import PermissionDenied


# Оголошуємо міксін, який перевіряє, чи є користувач власником обʼєкта
class UserIsOwnerMixin(object):
    # Перевизначаємо метод dispatch,
    # який викликається перед обробкою будь-якого HTTP-запиту (GET, POST тощо)
    def dispatch(self, request, *args, **kwargs):
        # Отримуємо обʼєкт, з яким працює view (наприклад, модель)
        instance = self.get_object()
        # Перевіряємо, чи поточний користувач є творцем (власником) обʼєкта
        if instance.creator != self.request.user:
            # Якщо ні — забороняємо доступ і повертаємо помилку 403
            raise PermissionDenied
        # Якщо перевірка пройшла успішно,
        # передаємо керування стандартному dispatch методу
        return super().dispatch(request, *args, **kwargs)
