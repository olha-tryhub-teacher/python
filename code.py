
# Напиши функцію high_rise
from random import randint
from turtle import *
from art import *


def high_rise2D(x, y, a, b, col1, col2):
    # Малюємо основу будинку
    start(x, y)
    width(4)
    rectangle_fill(a, b, col1)

    # Розрахунок розмірів та кількості вікон
    win_size = a // 6
    n = b // win_size
    x, y = x + win_size // 2, y + win_size // 2
    x0 = x

    # Малюємо вікна
    width(1)
    for i in range(n // 2):
        for j in range(3):
            start(x, y)

            # Визначаємо, чи горить світло
            if randint(1, 3) == 1:
                win_color = "darkorange"
            else:
                win_color = col2

            # Малюємо вікно з обраним кольором
            square_fill(win_size, win_color)
            x += 2 * win_size

        x = x0
        y += 2 * win_size


speed(0)
high_rise2D(0, -150, 80, 140, "grey", "orange")
