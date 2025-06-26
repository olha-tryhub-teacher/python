from cross_zeroes import *
from random import randint

game = True
player = randint(0, 1)

field(xStart, yStart, size, "black")

while game:
    if player == 0:
        movePlayer(player, zero)
        player = 1
    else:
        movePlayer(player, cross)
        player = 0
    win = checkWin()
    if win != -1:
        if win == 1:
            print("Виграв Хрестик!")
        else:
            print("Виграв Нулик!")
        game = False
