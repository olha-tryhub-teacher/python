# підключи молуль черепашки
from turtle import *
# підключи свій модуль guess
from guess import *
# підключи функцію випадковго вибору з модуля випадковості
from random import choice


# слова для гри, можна замінити на свої
words = ["папуга", "школа", "карета", "відео", "намисто","шоколадка", "калина", "пшениця", "врожай", "тризуб", "карпати", "прапор", "жито", "соловей", "бандура", "барвінок"]


# викличу функцію малювання завдання

# ігровий цикл
word = choice(words)
countRight = 0
countWrong = 0
xWrong, yWrong = -170, 50
speed(0)
setup(1000, 700)
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
        print("Ти не вгадав!!")
        break
    if countRight == len(word):
        print("Ти вгадав!!")
        break
