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

done()
