from turtle import *

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


def square_fill(a, col):
    color(col)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def rectangle_fill(a, b, col):
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


def circle_fill(a, col):
    color(col)
    begin_fill()
    circle(a)
    end_fill()


size = 100
xStart = -150
yStart = 150

xCor = [xStart + i * size for i in range(3)]  # x для 1, 2, 3 клітинки
yCor = [yStart - i * size for i in range(3)]  # y для верхнього, середнього, нижнього ряду

playingField = [-1, -1, -1, -1, -1, -1, -1, -1, -1]


def field(xStart, yStart, size, col):
    width(4)
    x, y = xStart, yStart
    for i in range(3):
        for j in range(3):
            start(x, y)
            square(size, col)
            x += size
        x = xStart
        y -= size


def cross(x, y, size, col):
    color(col)
    start(x, y)
    width(4)
    setheading(45)
    forward(1.4 * size)
    start(x + size, y)
    setheading(135)
    forward(1.4 * size)


def zero(x, y, size, col):
    start(x + size // 2, y)
    width(5)
    setheading(0)
    color(col)
    circle(size // 2)


def movePlayer(player, draw_function):
    if player == 0:
        print("Ходить нулик. Введіть номер клiтинки:")
        c = "#9b59b6"
    else:
        print("Ходить хрестик. Введіть номер клiтинки:")
        c = "#e74c3c"
    cell = int(input())

    while playingField[cell - 1] != -1:
        print("Ця клітинка вже зайняти. Оберіть іншу!")
        cell = int(input())
    cell = cell - 1
    i, j = cell % 3, cell // 3
    x, y = xCor[i], yCor[j]
    draw_function(x, y, size, c)
    playingField[cell] = player

def checkCells(n1, n2, n3):
    if (playingField[n1] == playingField[n2] and playingField[n2] == playingField[n3]):
        return playingField[n1]
    else:
        return -1

def checkWin():
    if checkCells(0, 1, 2) != -1:
        return checkCells(0, 1, 2)
    elif checkCells(3, 4, 5) != -1:
        return checkCells(3, 4, 5)
    elif checkCells(6, 7, 8) != -1:
        return checkCells(6, 7, 8)
    elif checkCells(0, 3, 6) != -1:
        return checkCells(0, 3, 6)
    elif checkCells(1, 4, 7) != -1:
        return checkCells(1, 4, 7)
    elif checkCells(2, 5, 8) != -1:
        return checkCells(2, 5, 8)
    elif checkCells(0, 4, 8) != -1:
        return checkCells(0, 4, 8)
    elif checkCells(2, 4, 6) != -1:
        return checkCells(2, 4, 6)
    else:
        return -1
