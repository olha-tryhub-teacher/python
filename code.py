from turtle import *
from art import *

speed(0)
ht()


def cross(x, y, size, col):
    color(col)
    start(x, y)
    width(4)
    setheading(45)
    forward(1.4 * size)
    start(x + size, y)
    setheading(135)
    forward(1.4 * size)

cross(150, 0, 120, "green")
