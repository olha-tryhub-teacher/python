def cross(x, y, size, col):
    penup()
    goto(x, y)  # початкова позиція
    pendown()
    color("black","blue")
    width(2)
    begin_fill()
    setheading(-90)
    circle(25, 180)
    left(30)
    forward(50)
    left(120)
    forward(50)
    end_fill()
