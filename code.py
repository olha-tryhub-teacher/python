from turtle import *
from art import *

def cloud(x, y, a, col):
    start(x, y)
    width(1)
    color(col)
    begin_fill()
    for i in range(5):
        circle(a, 230)
        rt(199)
    end_fill()

cloud(0, 0, 30, "#0a279a")
