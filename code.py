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
