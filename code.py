from turtle import *
from art import *
speed(100)
pixel_size = 10
x,y = -100,100
for line in pic_map:
    for num in line:
        start(x,y)
        c = colors_map[int(num)]
        square_fill(pixel_size,c)
        x+=pixel_size
    x = -100
    y -= pixel_size 
