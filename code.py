from turtle import *
from art import *


def square_fill(a, col):
    begin_fill()
    square(a, col)
    end_fill()


def rectangle_fill(a, b, col):
    begin_fill()
    rectangle(a, b, col)
    end_fill()


def triangle_fill(a, col):
    begin_fill()
    triangle(a, col)
    end_fill()


def parallelogram_fill(a, b, col):
    begin_fill()
    parallelogram(a, b, col)
    end_fill()


def polygon_fill(a, n, col):
    begin_fill()
    polygon(a, n, col)
    end_fill()


def circle_fill(a, col):
    color(col)
    begin_fill()
    circle(a)
    end_fill()
