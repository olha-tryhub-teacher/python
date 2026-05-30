# Напиши функцію christmas_tree
from turtle import *
from art import *

def christmas_tree(x, y, a, col1, col2):
    # Малюємо стовбур
    start(x, y)
    width(1)
    square_fill(a, col1)

    # Малюємо гілки (три яруси)
    x, y = x - a, y + a
    width(1)
    for i in range(3):
        start(x, y)
        # Передаємо col2 як колір хвої
        triangle_fill(a * 3, col2)
        y += a

speed(0)
# Приклад виклику:
christmas_tree(0, -100, 30, "brown", "green")
