from turtle import *

playingField = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

def move_player(player, draw_function):
    if player == 0:
        print("Ходить нулик.Введіть номер клiтинки:")
        c = "#9b59b6"
    else:
        print("Ходить хрестик.Введіть номер клiтинки:")
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
