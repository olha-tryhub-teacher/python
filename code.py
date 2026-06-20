# Функція для малювання пелюстки внизу і перемалювання всіх інших
def draw_down_petal(colors, col):
    draw_flower(colors)
    xd = randint(x_start - 50, x_start + 50)
    start(xd, y_start)
    h = randint(180, 360)
    setheading(h)
    width(20)
    draw_petal(col, r)
