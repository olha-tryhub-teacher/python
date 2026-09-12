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
