
# ваш код
# Координати кімнат, кольори, назви
data_room1 = (-100, 50, 100, 50, "green", "Кімната 1")
data_room2 = (-100, 100, 100, 50, "green", "Кімната 2")
data_living = (-100, -50, 100, 100, "white", "Вітальня")
data_corridor = (0, -50, 50, 200, "pink", "Коридор")
data_toilet = (50, -50, 80, 40, "yellow", "Туалет")
data_bath = (50, -10, 80, 80, "yellow", "Ванна")
data_kitchen = (50, 70, 80, 80, "violet", "Кухня")

# Загальний план будинку (список усіх кімнат)
plan_house = [
    data_room1, data_room2,
    data_living, data_corridor,
    data_toilet, data_bath,
    data_kitchen
]

from turtle import *


class Room:
    def __init__(self, x, y, w, h, bg_color, name):
        """Ініціалізація кімнати"""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bg_color = bg_color
        self.name = name

        # Окремий Turtle для кожної кімнати
        self.t = Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.t.width(10)
        self.t.color("purple", self.bg_color)  # Колір рамки і заповнення

    def go_to(self, x, y):
        """Переміщення без малювання"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def draw(self):
        """Малює кімнату з підписом"""
        self.go_to(self.x, self.y)

        # Малювання прямокутника
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(self.w)
            self.t.left(90)
            self.t.forward(self.h)
            self.t.left(90)
        self.t.end_fill()

        # Запис назви кімнати
        self.t.color("black")
        if self.w < self.h:  # Якщо кімната вертикальна — пишемо по вертикалі
            y_char = self.y + self.h - 45
            for char in self.name:
                self.go_to(self.x + 15, y_char)
                self.t.write(char, font=("Arial", 14))
                y_char -= 20
        else:  # Інакше пишемо по горизонталі
            self.go_to(self.x + 5, self.y + self.h // 3)
            self.t.write(self.name, font=("Arial", 14))


class House:
    def __init__(self, rooms_data_list):
        """Створює всі кімнати за планом"""
        self.rooms = []
        for room in rooms_data_list:
            r = Room(room[0], room[1], room[2], room[3], room[4], room[5])
            self.rooms.append(r)

        # Окремий Turtle для контуру будинку
        self.h = Turtle()
        self.h.speed(0)

    def skyline(self):
        """Малює зовнішній контур будинку"""
        self.h.width(15)
        self.h.color("purple")
        self.h.hideturtle()
        self.h.penup()
        self.h.goto(-100, -50)
        self.h.pendown()
        for i in range(2):
            self.h.forward(150 + 80)
            self.h.left(90)
            self.h.forward(200)
            self.h.left(90)

    def draw(self):
        """Малює всі кімнати та контур"""
        for room in self.rooms:
            room.draw()
        self.skyline()


# Створюємо будинок і малюємо його
house = House(plan_house)
house.draw()
