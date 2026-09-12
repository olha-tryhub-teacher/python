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
