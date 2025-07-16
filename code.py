from turtle import *

# Встановити швидкість черепашки
# speed(100)
tracer(5)  # пришвидшує візуалізацію
hideturtle()  # ховає стрілку

# Фон та кольори
colors_map1 = ["#0cf5f1", "#f50c0c", "#400a04", "#f2bbaa", "#050100", "#1921bf", "#e1f50a"]

# Малюнок (піксельна карта)
pic_map1 = [
    "---111111---",
    "--111111111-",
    "--2223343---",
    "-2323334333-",
    "-23223334333",
    "-2333344444-",
    "---333333---",
    "--11511511--",
    "-1115115111-",
    "111155551111",
    "331565565133",
    "335555555533",
    "--555--555--",
    "-222----222-",
    "2222----2222"
]

pixel_size = 10



pixel_size = 10

# Малює квадрат із заданим кольором без контуру
def square_fill(size, color):
    penup()
    begin_fill()
    fillcolor(color)
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()

# Переміщення до точки
def start(x, y):
    penup()
    goto(x, y)

# Основна функція малювання з піксельної карти
def drawPix(x, y, pic_map, colors_map):
    x_start = x
    for line in pic_map:
        for num in line:
            start(x, y)
            if num != "-":
                setheading(0)  # скидання напрямку
                square_fill(pixel_size, colors_map[int(num)])
            x += pixel_size
        x = x_start
        y -= pixel_size

# Заливка фону бірюзовим кольором
start(-400, 400)
square_fill(2000, "#4d97ff")

# Малювання піксельного зображення
drawPix(-200, 0, pic_map1, colors_map1)

