from turtle import Turtle, done, ht

ht()  # Ховаємо базову черепашку


# 1. Клас Пера
class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed(0)
        self.color("black")
        self.width(2)
        self.ondrag(self.goto)

    def increase_width(self):
        self.width(self.width() + 2)

    def decrease_width(self):
        if self.width() > 2:
            self.width(self.width() - 2)


# 2. БАЗОВИЙ КЛАС для будь-якої кнопки на панелі
class Button(Turtle):
    def __init__(self, x, y, shape, col, name):
        super().__init__()
        self.pu()
        self.speed(0)
        self.shape(shape)
        self.color(col)
        # Спершу йдемо трохи правіше і пишемо текст
        self.goto(x + 15, y - 8)
        self.write(name, font=("Arial", 12, "normal"))
        # Потім повертаємося на місце самої кнопки
        self.goto(x, y)


# 3. Клас кнопки кольору (успадковує базову кнопку)
class ColorButton(Button):
    def __init__(self, x, y, col, name, pen_object):
        # Викликаємо ініціалізацію базової кнопки
        super().__init__(x, y, "circle", col, name)
        self.pen = pen_object
        self.onclick(self.change_color)

    def change_color(self, x, y):
        self.pen.color(self.fillcolor())


# 4. Клас кнопки дії (успадковує базову кнопку)
class ActionButton(Button):
    def __init__(self, x, y, col, name, action_func):
        # Викликаємо ініціалізацію базової кнопки
        super().__init__(x, y, "square", col, name)

        self.action_func = action_func
        self.onclick(self.do_action)

    def do_action(self, x, y):
        self.action_func()


# === ОСНОВНА ПРОГРАМА ===

pen = Pen()

sidebar_x = -250  # Координата X для всієї бічної панелі (зліва)

# Створюємо кнопки кольорів
ColorButton(sidebar_x, 200, "black", "Чорний", pen)
ColorButton(sidebar_x, 160, "red", "Червоний", pen)
ColorButton(sidebar_x, 120, "blue", "Синій", pen)
ColorButton(sidebar_x, 80, "green", "Зелений", pen)
ColorButton(sidebar_x, 40, "orange", "Помаранчевий", pen)
# Створюємо кнопки дій
ActionButton(sidebar_x, 0, "darkgrey", "Товстіше", pen.increase_width)
ActionButton(sidebar_x, -40, "lightgrey", "Тонше", pen.decrease_width)
ActionButton(sidebar_x, -80, "red", "Очистити", pen.clear)

done()
