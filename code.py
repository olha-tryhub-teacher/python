#підключи свій модуль art
from turtle import*

def start(x, y):
    penup()
    goto(x, y)
    pendown()


def square(a, col):
    color(col)
    for i in range(4):
        fd(a)
        lt(90)


def rectangle(a, b, col):
    color(col)
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)


def triangle(a, col):
    color(col)
    for i in range(3):
        fd(a)
        lt(120)

def parallelogram(a, b, col):
    color(col)
    for i in range(2):
        fd(a)
        lt(125)
        fd(b)
        lt(55)


def polygon(a, n, col):
    color(col)
    angel = 360 / n
    for i in range(n):
        fd(a)
        lt(angel)


def circle(a, col):
    color(col)
    circle(a)


def square_fill(a, col):
  color(col)
  begin_fill()
  for i in range(4):
    fd(a)
    lt(90)
  end_fill()
    
    
def rectangle_fill(a,b, col):
  color(col)
  begin_fill()
  for i in range(2):
    fd(a)
    lt(90)
    fd(b)
    lt(90)
  end_fill()
  
  
def triangle_fill(a, col):
  color(col)
  begin_fill()
  for i in range(3):
    fd(a)
    lt(120)
  end_fill()
  
  
def parallelogram_fill(a, b, col):
  color(col)
  begin_fill()
  for i in range(2):
    fd(a)
    lt(125)
    fd(b)
    lt(55)
  end_fill()
  
  
def polygon_fill(a, n, col):
  color(col)
  angel = 360 / n
  begin_fill()
  for i in range(n):
    fd(a)
    lt(angel)
  end_fill()
  
def circle_fill(a,col):
  color(col)
  begin_fill()
  circle(a)
  end_fill()
