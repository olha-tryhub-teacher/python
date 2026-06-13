def check_win():
    # 1 = 2 = 3
    if playing_field[1] == playing_field[2] == playing_field[3] :
        return playing_field[1]
    # 4 = 5 = 6
    if playing_field[4] == playing_field[5] == playing_field[6] :
        return playing_field[4]
    # 7 = 8 = 9
    if playing_field[7] == playing_field[8] == playing_field[9] :
        return playing_field[7]
    # 1 = 4 = 7
    if playing_field[1] == playing_field[4] == playing_field[7] :
        return playing_field[1]
    # 2 = 5 = 8
    if playing_field[2] == playing_field[5] == playing_field[8] :
        return playing_field[2]
    # 3 = 6 = 9
    if playing_field[3] == playing_field[6] == playing_field[9] :
        return playing_field[3]
    # 1 = 5 = 9
    if playing_field[1] == playing_field[5] == playing_field[9] :
        return playing_field[1]
    # 3 = 5 = 7
    if playing_field[3] == playing_field[5] == playing_field[7] :
        return playing_field[3]

    return -1  # Ніхто не виграв
