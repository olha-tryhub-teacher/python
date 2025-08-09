from turtle import *
from time import sleep
from random import randint, choice


def create_t(x, y, form, col):
    t = Turtle()
    t.penup()
    t.goto(x, y)
    t.shape(form)
    t.color(col)
    return t


t_list = []
forms = ['triangle', 'square']
colors = ['red', 'yellow', 'green', 'blue']

for i in range(20):
    t1 = create_t(randint(-200, 200), randint(-200, 200), choice(forms), choice(colors))
    t_list.append(t1)

for i in range(50):
    for t in t_list:
        t.hideturtle()
    sleep(randint(0.1, 0.5))
    for t in t_list:
        t.showturtle()
    sleep(randint(0.1, 0.5))
