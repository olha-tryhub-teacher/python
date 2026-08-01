# 1
from turtle import *
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.color("black")
t2.color("red")
t3.color("orange")

t1.width(50)
t2.width(50)
t3.width(50)

t1.penup()
t1.goto(-150,50)
t1.pendown()
t1.fd(300)

t2.penup()
t2.goto(-150,0)
t2.pendown()
t2.fd(300)

t3.penup()
t3.goto(-150,-50)
t3.pendown()
t3.fd(300)
