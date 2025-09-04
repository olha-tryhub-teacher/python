# ваш код
from turtle import *
from random import randint

hideturtle()


def create_t(x, y, h, col):
    t = Turtle()
    t.color(col)
    t.shape("turtle")
    t.setheading(h)
    t.penup()
    t.goto(x, y)
    t.pendown()
    return t


# 1.Ігрове поле
screen = getscreen()
screen.bgcolor("yellow")

# 2.Лейбли-лічильник
click = create_t(200, 100, 0, "blue")
click.count = 0
click.hideturtle()
click.write(f"Click: {click.count}", font=("Arial", 24))

# те саме тільки раннер
runner = create_t(200, 150, 0, "red")
runner.count = 0
runner.hideturtle()
runner.write(f"Runner: {runner.count}", font=("Arial", 24))

# 3.Черепашки-втікачки
# 3.1 створити черепашок
t1 = create_t(0, 0, 0, "medium slate blue")
t2 = create_t(0, 0, 90, "dodger blue")
t3 = create_t(0, 0, 180, "lime")
t4 = create_t(0, 0, 270, "deep pink")


# 3.2 функції-обробники кліку
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
        t1.forward(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))


# 5. Переврка виграшу/програшу
if click.count >= 20:
    click.penup()
    click.goto(0, 0)
    click.write("You winn", font=("Arial", 40))
# те саме тільки раннер
if runner.count >= 4:
    runner.penup()
    runner.goto(0, 0)
    runner.write("You lose", font=("Arial", 40))


done()
