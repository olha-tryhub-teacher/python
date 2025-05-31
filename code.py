from art import *
from turtle import *
speed(100)
pixel_size = 10
x,y = -100,100
for line in pic_map:
    for num in line:
        penup()
        goto(x,y)
        pendown()
        c = colors_map[int(num)]
        square_fill(pixel_size,c)
        x+=pixel_size
    x = -100
    y -= pixel_size
