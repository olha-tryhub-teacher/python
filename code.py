# побудувати трасу, де є старт та фініш
def track():
    tr = create_turtle(-150, -150, "triangle", "green")
    tr.pd()
    tr.setheading(90)
    tr.fd(300)
    tr.color("red")
    tr.width(20)
    tr.pu()
    tr.goto(300, -150)
    tr.pd()
    tr.setheading(90)
    tr.fd(300)
