# модудь для гри, якмй будемо удосконалювати

sdvig = 200

from turtle import *

coordinats = ["370;-100", "390;-100", "390;110", "340;110",
              "300;110", "310;80", "305;20", "340;18",
              "320;15", "330;15", "330;-41", "330;-41"]


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
        start(100 + sdvig, 200)
        goto(120 + sdvig, 150)
        # 2
    elif count == 2:
        start(120 + sdvig, 150)
        goto(120 + sdvig, 50)
        # 3
    elif count == 3:
        start(120 + sdvig, 50)
        goto(150 + sdvig, 0)
        # 4
    elif count == 4:
        start(150 + sdvig, 0)
        goto(100 + sdvig, -50)
        # 5
    elif count == 5:
        start(100 + sdvig, -50)
        goto(50 + sdvig, 0)
        # 6
    elif count == 6:
        start(50 + sdvig, 0)
        goto(80 + sdvig, 50)
        # 7
    elif count == 7:
        start(80 + sdvig, 50)
        goto(80 + sdvig, 150)

        # 8
    elif count == 8:
        start(80 + sdvig, 150)
        goto(100 + sdvig, 200)
        # 9
    elif count == 9:
        start(100 + sdvig, -50)
        goto(100 + sdvig, 0)
        # 10
    elif count == 10:
        start(50 + sdvig, 0)
        goto(100 + sdvig, 0)
        # 11
    elif count == 11:
        start(100 + sdvig, 0)
        goto(175 + sdvig, 50)

        # 12
    elif count == 12:
        start(175 + sdvig, 50)
        goto(150 + sdvig, 60)

    elif count == 13:
        start(150 + sdvig, 60)
        goto(160 + sdvig, 150)

    elif count == 14:
        start(160 + sdvig, 150)
        goto(200 + sdvig, 200)

    elif count == 15:
        start(200 + sdvig, 200)
        goto(200 + sdvig, 0)

    elif count == 16:
        start(200 + sdvig, 0)
        goto(0 + sdvig, 0)

    elif count == 17:
        start(0 + sdvig, 0)
        goto(0 + sdvig, 200)

    elif count == 18:
        start(0 + sdvig, 200)
        goto(40 + sdvig, 150)

    elif count == 19:
        start(40 + sdvig, 150)
        goto(50 + sdvig, 60)

    elif count == 20:
        start(50 + sdvig, 60)
        goto(25 + sdvig, 50)

    elif count == 21:
        start(25 + sdvig, 50)
        goto(100 + sdvig, 0)


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


# сама гра, треба буде вставити у кружечок "Проєкт"
# підключи молуль черепашки
from turtle import *
# підключи функцію фипадковго вибору з модуля випадковості
from gerbenytsa import *
# підключи свій модуль gowlls
from random import choice

# координати частин шибениці
coordinats = ["370;-100", "390;-100", "390;110", "340;110",
              "300;110", "310;80", "305;20", "340;18",
              "320;15", "330;15", "330;-41", "330;-41"]

# слова для гри, можна замінити на свої
words = ["папуга", "школа", "карета", "відео", "намисто","шоколадка", "калина", "пшениця", "врожай", "тризуб", "карпати", "прапор", "жито", "соловей", "бандура", "барвінок"]


# створи усі необхідні змінні
def fon(col1, col2):
    penup()
    goto(-450, 200)
    pendown()
    width(450)
    color(col1)
    fd(900)

    penup()
    goto(-450, -200)
    pendown()
    width(400)
    color(col2)
    fd(900)


# викличу функцію малювання завдання

# ігровий цикл
word = choice(words)
countRight = 0
countWrong = 0
xWrong, yWrong = -170, 50
speed(0)
setup(1000, 700)
fon("#005eb8", "#ffd101")
writeAsk(word)

while True:
    letter = input("Введіть літеру:")
    if letter in word:
        c = writeRight(letter, word)
        countRight += c
    else:
        penup()
        goto(xWrong, yWrong)
        pendown()
        if xWrong < 50:
            xWrong += 45
        else:
            xWrong, yWrong = -170, yWrong - 45
        writeWrong(letter)
        countWrong += 1
        drawGalows(countWrong)

    if countWrong == 21:
        print("ne potughnyu progrash!")
        break
    if countRight == len(word):
        print("potughna peremoga!")
        break
