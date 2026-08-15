from random import randint, choice
from turtle import *

class Ball(Turtle):
    COLORS = ["red", "blue", "green", "yellow", "orange", "pink"]

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.setheading(270)
        self.respawn()

    def respawn(self):
        """Скидає кульку нагору у випадкову X-позицію та змінює колір."""
        self.goto(randint(-300, 300), 180)
        self.color(choice(self.COLORS))

    def move(self):
        """Рухає кульку вниз та перевіряє досягнення межі."""
        self.forward(10)
        if self.ycor() < -180:
            self.respawn()
        screen.ontimer(ball.move, 100)


# --- Налаштування екрана та запуск ---
screen = Screen()
ball = Ball()


ball.move()

done()
