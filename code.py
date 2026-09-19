# ваш код
from turtle import *
from random import randint


def create_turtle(x, y, sh, col):
    t = Turtle()
    t.pu()
    t.goto(x, y)
    t.width(10)
    t.shape(sh)
    t.color(col)
    return t


# побудувати трасу, де є старт та фініш
def track():
    tr = create_turtle(-150, -150, "triangle", "green")
    tr.setheading(90)
    tr.pendown()
    tr.forward(300)
    tr.color("red")
    tr.width(20)
    tr.penup()
    tr.goto(300, -150)
    tr.pendown()
    tr.forward(300)


def win(t):
    t.write("i am a winner!")


# створити черепашок
t1 = create_turtle(-150, 70, "turtle", "purple")
t2 = create_turtle(-150, -70, "turtle", "orange")

track()

# створити ігровий цикл, де черепашки будуть змагатись
while t1.xcor() < 300 and t2.xcor() < 300:
    t1.forward(randint(1, 7)) # 7
    t2.forward(randint(1, 7)) # 1


if t1.xcor() > t2.xcor(): #305, 301
    win(t1)
else:
    win(t2)

done()
