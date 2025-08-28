# побудувати трасу, де є старт та фініш
def track():
    tr = create_turtle(-150, -150, "triangle", "green")
    tr.penup()
    tr.setheading(90)
    tr.pendown()
    tr.forward(300)
    tr.color("red")
    tr.width(20)
    tr.penup()
    tr.goto(300, -150)
    tr.pendown()
    tr.setheading(90)
    tr.forward(300)
