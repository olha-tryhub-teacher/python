from turtle import Screen, Turtle, done
from random import randint, choice

# 1. Клас гравця
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("violet")
        self.penup()
        self.goto(0, -130)

    def move_l(self):
        if self.xcor() > -130:
            self.setx(self.xcor() - 15)

    def move_r(self):
        if self.xcor() < 130:
            self.setx(self.xcor() + 15)

# 2. Клас яблука
class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(choice(["red", "gold", "blue"]))
        self.goto(randint(-130, 130), 150)

    def fall(self):
        self.sety(self.ycor() - 5)

# 3. Налаштування екрана
screen = Screen()
screen.bgcolor("black")

# Малюємо біле поле за допомогою циклу (працює в усіх браузерах)
pole = Turtle()
pole.hideturtle()
pole.color("white")
pole.penup()
pole.goto(-150, 150)
pole.begin_fill()
for _ in range(4):
    pole.forward(300)
    pole.right(90)
pole.end_fill()

player = Player()
screen.listen()
screen.onkey(player.move_l, "Left")
screen.onkey(player.move_r, "Right")

# Лічильники та текст
score = {"catch": 0, "miss": 0}
writer = Turtle()
writer.hideturtle()
writer.color("white")
writer.penup()

def update_score():
    writer.clear()
    writer.goto(-140, 160)
    writer.write(f"Miss: {score['miss']}  Catch: {score['catch']}", font=("Arial", 16, "normal"))

update_score()
apples = []

# 4. Ігровий цикл
def game_loop():
    if randint(1, 25) == 1:
        apples.append(Apple())

    for apple in apples[:]:
        apple.fall()

        # Спіймано
        if apple.distance(player) < 20:
            apple.hideturtle()
            apples.remove(apple)
            score["catch"] += 1
            update_score()

        # Впало за межі
        elif apple.ycor() < -150:
            apple.hideturtle()
            apples.remove(apple)
            score["miss"] += 1
            update_score()

    # Перевірка кінця гри
    if score["miss"] >= 3:
        writer.goto(-60, 0)
        writer.write("You lose", font=("Arial", 20, "bold"))
    elif score["catch"] >= 10:
        writer.goto(-50, 0)
        writer.write("You win", font=("Arial", 20, "bold"))
    else:
        screen.ontimer(game_loop, 30)

game_loop()

done()



