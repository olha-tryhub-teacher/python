hideturtle()


def create_t(x, y, sh, col):
    t = Turtle()
    t.speed(0)
    t.penup()
    t.color(col)
    t.shape(sh)
    t.setheading(270)
    t.goto(x, y)
    return t
