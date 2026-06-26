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


def drawGalows(count):
    color("yellow")
    width(10)
    # 1
    if count == 1:
        pass
        # 2
    elif count == 2:
        pass
        # 3
    elif count == 3:
        pass
        # 4
    elif count == 4:
        pass
        # 5
    elif count == 5:
        pass
        # 6
    elif count == 6:
        pass
        # 7
    elif count == 7:
        pass
        # 8
    elif count == 8:
        pass
        # 9
    elif count == 9:
        pass
        # 10
    elif count == 10:
        pass


def writeAsk(word):
    start(-170, 100)
    setheading(0)
    width(4)
    color("black")
    for w in word:
        fd(30)
        penup()
        fd(15)
        pendown()


def writeWrong(letter):
    color("black")
    write(letter, font=("Arial", 28))
    color("red")
    width(2)
    setheading(45)
    fd(30)
    setheading(180)
    penup()
    fd(20)
    setheading(270 + 45)
    pendown()
    fd(30)
    color("grey")


def writeRight(letter, word):
    start(-170, 105)
    penup()
    color("black")
    setheading(0)
    count = 0
    for w in word:
        if w == letter:
            pendown()
            write(letter, font=("Arial", 32))
            penup()
            count += 1
        fd(45)
    return count


def getCor(cor):
    x, y = cor.split(";")  # "200;-100" -> ["200", "-100"]
    x, y = int(x), int(y)
    return x, y