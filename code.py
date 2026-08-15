from turtle import Turtle, done, ht
from random import randint


# 1. Функція для малювання ігрового поля
def draw_field():
    t = Turtle()
    t.ht()
    t.speed(0)
    t.color("gold")
    t.width(10)
    t.pu()
    t.goto(-150, -100)
    t.pd()
    for _ in range(2):
        t.fd(300)
        t.lt(90)
        t.fd(200)
        t.lt(90)


# 2. Клас для створення напису-позначки (успадковує Turtle)
class Label(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.ht()
        self.pu()
        self.color("violet")
        self.goto(x, y)

    def update_text(self, count):
        self.clear()
        self.write(f"In rect {count} turtle", font=("Arial", 16))


# 3. Клас для черепашок, які можна перетягувати (успадковує Turtle)
class DragTurtle(Turtle):
    def __init__(self, x, y, col):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.color(col)
        self.pu()
        self.goto(x, y)

        # Прив'язуємо подію перетягування до методу
        self.ondrag(self.on_drag)

    def on_drag(self, x, y):
        self.goto(x, y)
        check_turtles()  # Оновлюємо лічильник при кожному русі


# 4. Функція перевірки кількості черепашок у прямокутнику
def check_turtles():
    count = 0
    for t in turtles:
        # Перевіряємо координати відносно центру
        if abs(t.xcor()) < 150 and abs(t.ycor()) < 100:
            count += 1

    label.update_text(count)


# --- ОСНОВНА ЧАСТИНА ПРОГРАМИ ---

ht()  # Ховаємо стандартну черепашку
draw_field()

# Створюємо об'єкт напису
label = Label(-150, -125)

# Створюємо черепашок і додаємо їх у список
turtles = []
colors = ["red", "blue", "purple", "orange"]

for col in colors:
    # Зверніть увагу: я змінив randint(-150, -150) на randint(-150, 150),
    # щоб черепашки з'являлися у випадкових місцях по висоті.
    t = DragTurtle(randint(-200, 200), randint(-150, 150), col)
    turtles.append(t)

# Робимо першу перевірку одразу після появи черепашок
check_turtles()

done()
