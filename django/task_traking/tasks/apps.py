# Імпортуємо базовий клас AppConfig,
# який використовується для конфігурації Django-додатку
from django.apps import AppConfig


# Оголошуємо клас конфігурації для додатку "tasks"
class TasksConfig(AppConfig):

    # Вказуємо тип поля за замовчуванням для первинних ключів (id)
    # BigAutoField використовує 64-бітне число замість стандартного AutoField
    default_auto_field = 'django.db.models.BigAutoField'

    # Назва додатку, яка використовується Django
    # та повинна відповідати імені папки додатку
    name = 'tasks'
