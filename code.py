from turtle import *

ht()
max_x, max_y = 170, 120  # Межі робочої області


# === УТИЛІТИ ===


# Створення черепашки з заданими параметрами
def create_t(x, y, sh, col):
    t = Turtle()
    t.shape(sh)
    t.speed(0)
    t.color(col)
    goto_clear(t, x, y)
    return t


# Переміщення черепашки без сліду
def goto_clear(t, x, y):
    t.pu()
    t.goto(x, y)
    t.pendown()


# Малювання прямокутника заданого розміру
def draw_rect(t, a, b):
    for _ in range(2):
        t.forward(a)
        t.lt(90)
        t.forward(b)
        t.lt(90)


# === СТВОРЕННЯ ОБ’ЄКТІВ ===


# Створення пера для малювання
def create_pen():
    t = create_t(0, 0, "turtle", "black")

    # Обробка перетягування мишкою
    def on_drag(x, y):
        if abs(x) < max_x and abs(y) < max_y:
            t.goto(x, y)

    t.ondrag(on_drag)

    # Збільшення товщини пера
    def width_plus_t():
        t.width(t.width() + 1)
        label_width.write_t(f"Width:{pen.width()}")

    # Зменшення товщини пера
    def width_minus_t():
        if t.width() > 0:
            t.width(t.width() - 1)
            label_width.write_t(f"Width:{pen.width()}")

    t.width_plus_t = width_plus_t
    t.width_minus_t = width_minus_t

    # Обробка кліку по полотну — переміщення пера
    def on_click(x, y):
        if abs(x) < max_x and abs(y) < max_y:
            goto_clear(t, x, y)

    t.on_click = on_click

    # Обробка клавіш для переміщення
    def move_left():
        t.setheading(180)
        t.forward(2)

    def move_right():
        t.setheading(0)
        t.forward(2)

    def move_up():
        t.setheading(90)
        t.forward(2)

    def move_down():
        t.setheading(270)
        t.forward(2)

    t.move_left = move_left
    t.move_right = move_right
    t.move_up = move_up
    t.move_down = move_down

    return t


# Створення текстової позначки
def create_label(x, y, col, txt):
    t = create_t(x, y, "turtle", col)
    t.hideturtle()

    # Виведення тексту
    def write_t(txt):
        t.clear()
        t.write(txt, font=("Arial", 16))

    t.write_t = write_t
    t.write_t(txt)
    return t


# Створення кнопки з подією
def create_button(x, y, sh, col, func):
    t = create_t(x, y, sh, col)
    t.my_color = col

    # Подія: натискання кнопки
    def on_click(x, y):
        t.color("black", t.my_color)  # коротка зміна кольору як візуальний ефект
        func()
        t.color(t.my_color)

    t.onclick(on_click)

    return t


# Створення кольорової кнопки (окрема логіка)
def create_btn_color(x, y, col):
    t = create_t(x, y, "circle", col)
    t.my_color = col

    # Подія: змінити колір пера
    def new_color(x, y):
        t.color("black", t.my_color)  # анімація натиснення
        pen.color(t.my_color)
        t.color(t.my_color)

    t.onclick(new_color)

    return t


# === ОФОРМЛЕННЯ ІНТЕРФЕЙСУ ===


# Малюємо основну рамку і панель
t = create_t(-1 * max_x, -1 * max_y, "turtle", "black")
t.hideturtle()
t.width(7)
t.pendown()
draw_rect(t, 2 * max_x, 2 * max_y)

# Верхня панель
goto_clear(t, -1 * max_x, max_y)
t.color("black", "violet")
t.begin_fill()
draw_rect(t, 2 * max_x, 60)
t.end_fill()


# === ОБРОБНИКИ ПОДІЙ ===


# Вмикання/вимикання заливки
def begin_end_fill():
    # grey - не активна, red - закінчити, green - почати
    if btn_fill.my_color == "grey" or btn_fill.my_color == "red":
        pen.begin_fill()
        col = "green"
        txt = "EF"  # End Fill
    else:
        pen.end_fill()
        col = "red"
        txt = "BF"  # Begin Fill
    btn_fill.color(col)
    btn_fill.my_color = col
    label_fill.color(col)
    label_fill.write_t(txt)


# === СТВОРЕННЯ ГОЛОВНИХ ЕЛЕМЕНТІВ ===


pen = create_pen()  # головне перо

# Кнопка очистки
label_clear = create_label(-164, 145, "white", "Clear")
btn_clear = create_button(-100, 152, "square", "white", pen.clear)

# Кнопка заливки
label_fill = create_label(-80, 145, "grey", "Fill")
btn_fill = create_button(-40, 152, "circle", "grey", begin_end_fill)

# Індикатор товщини пера + кнопки зміни
label_width = create_label(2, 145, "black", f"Width:{pen.width()}")
btn_width_plus = create_button(-10, 164, "square", "yellow", pen.width_plus_t)
btn_width_minus = create_button(-10, 140, "square", "blue", pen.width_minus_t)

# Кнопки зміни кольору
x, y = 90, 164
colors = ["navy", "purple", "gold", "lightgreen", "crimson", "dodger blue", "yellow", "black"]
for i in range(6):
    if i == 3:
        x, y = 90, 140  # перенесення на новий ряд
    btn_col = create_btn_color(x, y, colors[i])
    x += 30

# === ПІДПИСКА НА ПОДІЇ ===


screen = getscreen()
screen.onclick(pen.on_click)  # клік по робочій області — переміщення пера
screen.onkey(pen.move_left, "Left")  # стрілки — керування
screen.onkey(pen.move_right, "Right")
screen.onkey(pen.move_up, "Up")
screen.onkey(pen.move_down, "Down")
screen.listen()

done()
