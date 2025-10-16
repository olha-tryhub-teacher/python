from turtle import *


# --- Налаштування екрану ---
screen = Screen()
screen.bgcolor("lightblue")


# --- Базовий клас для всіх спрайтів ---
class Sprite(Turtle):
    def __init__(self, x, y, col, sh):
        super().__init__()
        # t = Turtle()
        self.color(col)
        self.shape(sh)
        self.go_to(x, y)


    # Переміщення спрайта без малювання
    def go_to(self, x, y):
        self.penup()
        self.goto(x, y)


    # Перевірка зіткнення з іншим об’єктом
    def touch_t(self, t):
        if abs(self.xcor() - t.xcor()) < 20 and abs(self.ycor() - t.ycor()) < 20:
            return True
        return False


# --- Клас гравця (керується з клавіатури) ---
class Player(Sprite):
    def __init__(self, x, y, col, sh, step_size):
        super().__init__(x, y, col, sh)
        self.step_size = step_size


        # Прив'язка клавіш до функцій руху
        screen.onkey(self.move_left, "Left")
        screen.onkey(self.move_right, "Right")
        screen.onkey(self.move_down, "Down")
        screen.onkey(self.move_up, "Up")
        screen.listen()


    # Рух вліво
    def move_left(self):
        self.setheading(180)
        self.forward(self.step_size)


    # Рух вправо
    def move_right(self):
        self.setheading(0)
        self.forward(self.step_size)


    # Рух вгору
    def move_up(self):
        self.setheading(90)
        self.forward(self.step_size)


    # Рух вниз
    def move_down(self):
        self.setheading(270)
        self.forward(self.step_size)


    # Виведення повідомлення про завершення гри
    def write_end(self, txt):
        self.go_to(-150, 0)
        self.write(txt, font=("Arial", 30))


# --- Клас ворога, що рухається автоматично ---
class Enemy(Sprite):
    def __init__(self, x, y, col, sh, step_size):
        super().__init__(x, y, col, sh)
        self.step_size = step_size


    # Рух ворога вздовж осі X з відбиванням
    def move(self):
        self.forward(self.step_size)
        if self.xcor() >= 200:
            self.setheading(180)
            self.forward(self.step_size)
        if self.xcor() <= -200:
            self.setheading(0)
            self.forward(self.step_size)


# --- Створення об'єктів гри ---
enemy1 = Enemy(200, 100, "red", "square", 30)
enemy2 = Enemy(-200, -100, "red", "square", 30)
player = Player(0, -180, "navy", "turtle", 10)
finish = Sprite(0, 180, "gold", "triangle")


# --- Основна ігрова функція (цикл) ---
def game():
    # Рух ворогів
    enemy1.move()
    enemy2.move()


    # Перевірка програшу
    if player.touch_t(enemy1) or player.touch_t(enemy2):
        player.write_end("I am loose 😭😭😭")
        return


    # Перевірка виграшу
    if player.touch_t(finish):
        player.write_end("I am wiin 😁😁😁")
        return


    # Повторний запуск функції через 100 мс (таймер)
    screen.ontimer(game, 100)


# --- Запуск гри ---
game()

done()
