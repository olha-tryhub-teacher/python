from turtle import *
from art import *

def cloud(x, y, a, col):
  start(x, y)
  w = a//6
  start_line(w, col,col)
  fd(a)
  
  start(x+a//5, y)
  w = a//4
  start_line(w, col,col)
  fd(a - a//4)
  
  start(x+a//2, y)
  w = a//3
  start_line(w, col,col)
  fd(a // 3)
  
cloud(0,0,100,"#0a279a")
