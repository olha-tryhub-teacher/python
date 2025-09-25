import turtle


# Оголошення класу Painter (Малювальник)
class Painter:
    # Конструктор — створює об'єкт turtle, який ховається в приватному атрибуті __t
    def __init__(self):
        self.__t = turtle.Turtle()  # Створюється черепашка для малювання


    # Метод для переміщення черепашки в координати (x, y)
    def goto(self, x, y):
        self.__t.goto(x, y)


    # Метод для зміни кольору пера та заливки
    def set_color(self, color):
        self.__t.color(color)


    # Метод для встановлення напряму (в градусах)
    def heading(self, h):
        self.__t.setheading(h)


    # Метод для руху вперед на певну довжину
    def forward(self, length):
        self.__t.fd(length)


    # Метод для малювання прямокутника із заданою шириною, висотою та кольором
    def draw_rect(self, width, height, color):
        self.set_color(color)           # Встановити колір
        self.__t.begin_fill()           # Почати заливку
        for _ in range(2):              # Двічі пройти по двом сторонам прямокутника
            self.forward(width)         # Малюємо ширину
            self.__t.right(90)             # Повертаємось на 90 градусів вправо
            self.forward(height)        # Малюємо висоту
            self.__t.right(90)             # Повертаємось знову
        self.__t.end_fill()             # Завершуємо заливку


    # Метод для малювання круга з центром у (x, y), певним радіусом і кольором
    def draw_circle(self, x, y, radius, color):
        self.set_color(color)           # Встановити колір
        self.goto(x, y)                 # Переміститись у центр круга
        self.__t.begin_fill()           # Почати заливку
        self.__t.circle(radius)         # Намалювати круг заданого радіуса
        self.__t.end_fill()             # Завершити заливку

p1 = Painter()
p1.draw_circle(100, 100, 30, "yellow")
turtle.done()
