from turtle import *
from art import *

# підключи модуль turtle
# встанови швидкість(speed) черепашки - 0
speed(0)
tracer(9)
# перший малюнок - список кольорів
# блакитний0 червоний1 чорний2
colors_map1 = ["#87CEEB", "#FF0000", "#000000"]

# перший малюнок - закодований малюнок
pic_map1 = [
    "-22-22-",
    "2112112",
    "2111112",
    "-21112-",
    "--212--",
    "---2---",
]
# встановлюємо розмір пікселя
pixel_size = 8


# функція для малювання арту
def draw_pixel_art(x, y, pic_map, colors_map):
    x_start = x
    for line in pic_map:
        for num in line:
            start(x, y)
            if num != "-":
                square_fill(pixel_size, colors_map[int(num)])
            x += pixel_size
        x = x_start
        y -= pixel_size


# малюємо арт
draw_pixel_art(-100, 100, pic_map1, colors_map1)
