def create_turtle(x, y, sh, col):
    t = Turtle()
    t.pu()
    t.goto(x, y)
    t.width(10)
    t.shape(sh)
    t.color(col)
    return t
