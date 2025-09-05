from turtle import *
from random import randint, choice

ht()


def create_t(x, y, sh, col):
    t = Turtle()
    t.speed(0)
    t.pu()
    t.color(col)
    t.shape(sh)
    t.setheading(270)
    t.goto(x, y)
    return t
screen = getscreen()


# ваш код
# 1. Ігрове поле
screen.bgcolor("black")
pole = create_t(-150, 150, "turtle", "white")
pole.ht()
pole.begin_fill()
for _ in range(4):
    pole.fd(300)
    pole.lt(90)
pole.end_fill()

# 2. Лейбли - лічильники
# 2.1 Створити лейбли
miss = create_t(-150, 160, "turtle", "red")
miss.count = -1
miss.ht()
catch = create_t(70, 160, "turtle", "green")
catch.count = -1
catch.ht()


# 2.2 Функція що оновлює напис
def update_count(label, txt):
    label.count += 1
    label.clear()
    label.write(f"{txt} : {label.count}", font=("Arial", 16))


# 3.Платформа-гравець
# 3.1 Створити гравця
plt = create_t(0, -130, "square", "violet")


# 3.2 Функції руху праворчу-ліворуч
def move_l():
    plt.setheading(180)
    plt.fd(10)

def move_r():
    plt.setheading(0)
    plt.fd(10)

# 3.3 Підписка на події клавіші
screen.onkey(move_l, "Left")
screen.onkey(move_r, "Right")
screen.listen()
# 4. Яблука
# 4.1 Список яблук
apples = []
colors = ["red", "gold", "blue"]


# 4.2 Функція появи нового яблука
def spawn_a():
    a = create_t(randint(-130, 130), 150, "circle", choice(colors))
    apples.append(a)


# 4.3 Функця руху яблука
def move(a):
    a.fd(5)


# 4.4 Функція перевірки яблука, що впало
def check_miss(a):
    if a.ycor() <= - 150:
        a.ht()
        apples.remove(a)
        update_count(miss, "Miss")


# 4.5 Функція спійманого яблука
def check_catch(a):
    x, y = plt.xcor(), plt.ycor()
    if a.distance(x, y) <= 10:
        a.ht()
        apples.remove(a)
        update_count(catch, "Catch")


# 5. Функція перевірка виграшу/програшу
def check_end_game():
    if miss.count >= 3:
        miss.goto(0, 0)
        miss.write("You lose", font=("Arial", 14))
        return True
    if catch.count >= 10:
        catch.goto(0, 0)
        catch.write("You lose", font=("Arial", 14))
        return True
    return False


# 6. Функція гри
def game():
    if randint(1, 30) == 3:
        spawn_a()
    for a in apples:
        move(a)
        check_miss(a)
        check_catch(a)
    end = check_end_game()
    if not end:
        screen.ontimer(game, 50)


# Запускаємо все
update_count(miss, "Miss")
update_count(catch, "Catch")
spawn_a()
game()

done()
