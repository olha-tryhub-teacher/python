from turtle import *
from gallows import *
from art import *
from random import choice

words = ["папуга", "школа", "карета", "відео", "намисто","шоколадка"]
word = choice(words)
countRight = 0
countWrong = 0
xWrong, yWrong = -170, 50

# setup(1000, 800)

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

    if countWrong == 12:
        print("Lose")
        break
    if countRight == len(word):
        print("Win")
        break
