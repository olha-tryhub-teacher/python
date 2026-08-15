
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
