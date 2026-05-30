# Малюємо квадрат
from turtle import *


def square(a, col):
    color(col)
    for i in range(4):
        fd(a)
        lt(90)


square(50, "red")
