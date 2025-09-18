from turtle import *
from random import randint

hideturtle()


def create_t(x, y, sh, col):
    t = Turtle()
    t.shape(sh)
    t.speed(0)
    t.color(col)
    t.penup()
    t.goto(x, y)
    return t


# 1.Функція - малюємо ігрове поле
def draw_field():
    t = create_t(-150, -100, "turtle", "gold")
    t.hideturtle()
    t.width(10)
    t.pendown()
    for _ in range(2):
        t.fd(300)
        t.lt(90)
        t.fd(200)
        t.lt(90)


# 2. Функція - створити об'єкт черепашка(координати та колір). Метод - перетягувати
def create_turtle(x, y, col):
    t = create_t(x, y, "circle", col)

    def on_drag(x, y):
        t.goto(x, y)
        check_turtle()

    t.ondrag(on_drag)
    return t


# 3. створити 4 об'єкта черепашки - список
turtle_list = []
colors = ["red", "blue", "purple", "orange"]
for col in colors:
    t = create_turtle(randint(-200, 200), -150, col)
    turtle_list.append(t)


# 4. Функція - створити напис-позначку, метод - оновлювати напис
def create_label(x, y):
    t = create_t(x, y, "turtle", "violet")
    t.hideturtle()

    def write_t(count):
        t.clear()
        t.write(f"In rect {count} turtle", font=("Arial", 16))

    t.write_t = write_t
    return t


# 5. Створити напис-позначку
label = create_label(-150, -125)


# 6.Функція - перевірити кількість черпашок у прямокутнику
def check_turtle():
    count = 0
    for t in turtle_list:
        if abs(t.xcor()) < 150 and abs(t.ycor()) < 100:
            count += 1

    label.write_t(count)


# 7. Намалювати ігрове поле, перевірити де черепашки піся спавну
draw_field()
check_turtle()

done()
