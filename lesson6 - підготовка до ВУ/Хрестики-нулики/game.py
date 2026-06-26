from turtle import *
from art import *
from cross import *
from random import randint

speed(0)
field("green")





player = randint(0, 1)
while True:

    if player == 1:
        move_player(player, "red")
        player = 0
    else:
        move_player(player, "yellow")
        player = 1

    win = check_win()
    if win == 1:
        print("Cross win")
        break
    elif win == 0:
        print("Dot win")
        break
