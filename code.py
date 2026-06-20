# Функція для малювання однієї пелюстки
def draw_petal(col, radius):
    color(col)
    begin_fill()
    circle(radius, 60)  # Півколо
    left(120)  # Поворот для іншої сторони
    circle(radius, 60)  # Півколо
    end_fill()


# Функція для малювання стовбура
def draw_stem():
    start(x_start, y_start)
    setheading(90)
    color("green")
    width(20)
    fd(50)
    setheading(135)
    draw_petal("green", 100)
    setheading(25)
    draw_petal("green", 65)
    setheading(90)
    fd(150)

# Функція для малювання пелюсток
def draw_petals(colors):
    # Малювання квітки
    width(20)
    k = starting_angle
    for i in range(7):
        start(x_start,y_start + 200)
        setheading(k)
        draw_petal(colors[i], r)
        k += starting_angle


# Функція для малювання всієї квітки
def draw_flower(colors):
    draw_stem()
    draw_petals(colors)
