from turtle import *

coordinats = ["370;-100","390;-100","390;110","340;110",
             "300;110","310;80","305;20","340;18",
             "320;15","330;15","330;-41","330;-41"]


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
    x, y = getCor(coordinats[count - 1])
    start(x, y)
    color("grey")
    width(10)
    # 1 ОСНОВА
    if count == 1:
        setheading(0)
        fd(40)
        # 2 СТОВП
    elif count == 2:
        setheading(90)
        fd(210)
        # 3  ПЕРЕКЛАДИНА 1
    elif count == 3:
        setheading(180)
        fd(95)
        # 4 ПЕРЕКЛАДИНА 2
    elif count == 4:
        setheading(270 + 45)
        fd(65)
        # 5 МОТУЗКА 1
    elif count == 5:
        setheading(270)
        fd(40)
        # 6 МОТУЗКА 2
    elif count == 6:
        width(5)
        setheading(0)
        for i in range(4):
            setheading(180)
            pendown()
            fd(20)
            penup()
            setheading(270)
            fd(5)
            setheading(0)
            pendown()
            fd(20)
        bk(10)
        setheading(270)
        fd(15)

        # 7 ГОЛОВА
    elif count == 7:
        width(3)
        circle(25)
        # ОЧІ ТА СУМНА УСМІШКА - НЕОБОВ’ЯЗКОВАЧАСТИНА
        start(x + 5, y + 30)
        setheading(270 + 45)
        fd(15)
        start(x + 10, y + 30)
        setheading(270 - 45)
        fd(15)
        start(x + 25, y + 30)
        setheading(270 + 45)
        fd(15)
        start(x + 31, y + 30)
        setheading(270 - 45)
        fd(15)
        start(x + 10, y)
        setheading(45)
        circle(-17, 100)

        # 8 РУКА 1
    elif count == 8:
        setheading(290)
        width(4)
        pendown()
        fd(45)
        # 9 РКА 2
    elif count == 9:
        width(4)
        setheading(250)
        pendown()
        fd(45)
        # 10 ТІЛО
    elif count == 10:
        setheading(0)
        width(4)
        pendown()
        setheading(270)
        fd(60)
        # 11 НОГА 1
    elif count == 11:
        width(4)
        setheading(270 - 45)
        fd(45)

        # 12 НОГА 2
    elif count == 12:
        width(4)
        setheading(270 + 45)
        fd(45)


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
    x, y = cor.split(";") # "200;-100" -> ["200", "-100"]
    x, y = int(x), int(y)
    return x, y
