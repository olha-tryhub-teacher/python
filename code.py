# Малюємо квадрат
from turtle import *


def square(a, col):
    color(col)
    for i in range(4):
        fd(a)
        lt(90)


square(50, "red")

# ⭐

def square(a, w, col):
    color(col)
    width(w)
    for i in range(4):
        fd(a)
        lt(90)


square(50, 10, "red")

# Створіть функцію rectangle
from turtle import *


def rectangle(a, b, col):
    color(col)
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)


rectangle(50, 30, "red")
# ⭐

def rectangle(a, b, w, col):
    color(col)
    width(w)
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)


rectangle(50, 90, 10, "red")

# Напишу функцію triangle.
from turtle import *


def triangle(a, col):
    color(col)
    for i in range(3):
        fd(a)
        lt(120)


triangle(50, "red")

# Напишіть функцію parallelogram
from turtle import *


def parallelogram(a, b, col):
    color(col)
    for i in range(2):
        fd(a)
        lt(125)
        fd(b)
        lt(55)


parallelogram(50, 120, "red")
# ⭐⭐
from turtle import *


def parallelogram(a, b, w, angel, col):
    color(col)
    width(w)
    angel2 = 180 - angel
    for i in range(2):
        fd(a)
        lt(angel)
        fd(b)
        lt(angel2)


parallelogram(50, 70, 10, 35, "red")

# Напишіть функцію polygon
from turtle import *


def polygon(a, n, col):
    color(col)
    angel = 360 / n
    for i in range(n):
        fd(a)
        lt(angel)


polygon(50, 5, "red")
# ⭐

def polygon(a, n, w, col):
    color(col)
    width(w)
    angel = 360 / n
    for i in range(n):
        fd(a)
        lt(angel)


polygon(50, 5, "red")

