# ваш код
from turtle import *
from random import randint
from time import sleep

ht()


def create_t(x, y, h, col):
    t = Turtle()
    t.color(col)
    t.shape("turtle")
    t.setheading(h)
    t.pu()
    t.goto(x, y)
    t.pd()
    return t


# 1.Ігрове поле
screen = getscreen()
screen.bgcolor("yellow")

# 2.Лейбли-лічильник
click = create_t(200, 100, 0, "blue")
click.count = 0
click.ht()
click.write(f"Click: {click.count}", font=("Arial", 24))

runner = create_t(200, 150, 0, "red")
runner.count = 0
runner.ht()
runner.write(f"Runner: {runner.count}", font=("Arial", 24))

# 3.Черепашки-втікачки
# 3.1 створити черепашок
t1 = create_t(0, 0, 0, "pink")
t2 = create_t(0, 0, 90, "violet")
t3 = create_t(0, 0, 180, "lightblue")
t4 = create_t(0, 0, 270, "gold")


# 3.2 функції-оброюники кліку
def click1(x, y):
    t1.lt(randint(30, 200))
    click.count += 1
    click.clear()
    click.write(f"Click: {click.count}", font=("Arial", 24))


def click2(x, y):
    t2.lt(randint(30, 200))
    click.count += 1
    click.clear()
    click.write(f"Click: {click.count}", font=("Arial", 24))


def click3(x, y):
    t3.lt(randint(30, 200))
    click.count += 1
    click.clear()
    click.write(f"Click: {click.count}", font=("Arial", 24))


def click4(x, y):
    t4.lt(randint(30, 200))
    click.count += 1
    click.clear()
    click.write(f"Click: {click.count}", font=("Arial", 24))


# 3.3 підписка на подію клік по черепашках
t1.onclick(click1)
t2.onclick(click2)
t3.onclick(click3)
t4.onclick(click4)

# 4. Ігровий цикл
while click.count < 20 and runner.count < 4:
    if abs(t1.xcor()) < 200 and abs(t1.ycor()) < 200:
        t1.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))

    if abs(t2.xcor()) < 200 and abs(t2.ycor()) < 200:
        t2.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))

    if abs(t3.xcor()) < 200 and abs(t3.ycor()) < 200:
        t3.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))

    if abs(t4.xcor()) < 200 and abs(t4.ycor()) < 200:
        t4.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))
    sleep(0.1)

# 5. Переврка виграшу/програшу
if click.count >= 20:
    click.pu()
    click.goto(0, 0)
    click.write("You winn", font=("Arial", 40))
if runner.count >= 4:
    runner.pu()
    runner.goto(0, 0)
    runner.write("You lose", font=("Arial", 40))


