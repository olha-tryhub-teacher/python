def draw_cloud_contour():
    penup()
    goto(-30, -10)  # початкова позиція
    pendown()
    color("black","white")
    width(4)
    speed(3)
    begin_fill()
    # Малюємо хмаринку з 5 перекриваючих дуг
    setheading(45)
    circle(15, 180)   # ліва маленька пухлина
    setheading(90)
    circle(25, 180)   # велика середня ліва
    setheading(145)
    circle(15, 180)   # центральна
    setheading(3)
    forward(90)
    end_fill()
    penup()
    hideturtle()
