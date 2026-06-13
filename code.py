def field(col):
    xStart,yStart = -150,50
    size = 100
    x,y = xStart, yStart
    for i in range(3):
        for j in range(3):
            start(x,y)
            square(size,10,col)
            x += size
        x = xStart
        y -= size
       
def draw_cross(x,y,col):
    size = 100
    start(x,y)
    color(col)
    width(10)
    setheading(45)
    fd(1.4*size)
    start(x+size, y)
    setheading(135)
    fd(1.4*size)
def draw_dot(x,y,col):
    start( x+size//2, y)
    setheading(0)
    color(col)
    circle( size//2)
   
def move_player(player, col):
    cell = int(input("Введіть номер клітинки від 1 до 9"))
    while playing_field[cell]!=-1:
        print("Клітинки вже зайнята!")
        cell = int(input("Введіть номер клітинки від 1 до 9"))
    x = x_cor[cell]
    y = y_cor[cell]
    start(x,y)
    playing_field[cell] = player
    color(col)
    if player == 1:
        draw_cross(x,y,col)
    else:
        draw_dot(x,y,col)
       
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


