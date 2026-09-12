class Answer(t.Turtle):
    def __init__(self, x1, y1, x2, y2, text, color_name, is_right):
        super().__init__()
        self.target = (x2, y2)
        self.is_right = is_right
        self.speed(0)
        self.color(color_name)
        self.penup()
        self.goto(x1, y1)
        self.showturtle()
        self.write(text, align="center", font=("Arial", 16, "normal"))

    def hide_answer(self):
        self.clear()
        self.hideturtle()

    def draw_path(self):
        self.clear()
        self.pendown()
        self.goto(self.target)
        self.hideturtle()


class Level:
    def __init__(self, data):
        self.answers = [
            Answer(x1, y1, x2, y2, text, COLORS[i], is_right)
            for i, (x1, y1, x2, y2, text, is_right) in enumerate(data)
        ]

    def clear_wrong_answers(self):
        for answer in self.answers:
            if not answer.is_right:
                answer.hide_answer()


class Player(t.Turtle):
    def __init__(self, game):
        super().__init__(shape="square")
        self.game = game
        self.color("green")
        self.speed(0)
        self.penup()
        self.goto(0, 0)

    def move(self, dx, dy):
        self.goto(self.xcor() + dx, self.ycor() + dy)
        self.check_collision()

    def check_collision(self):
        for answer in self.game.level.answers:
            if answer.isvisible() and self.distance(answer) < HIT_DISTANCE:
                if answer.is_right:
                    answer.draw_path()
                    self.game.next_level()
                else:
                    answer.hide_answer()
                    self.game.errors += 1
                return


class Game:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.bgcolor("white")
        self.screen.listen()

        self.writer = t.Turtle()
        self.writer.penup()
        self.writer.goto(-200, 150)

        self.level_index = 0
        self.errors = 0
        self.level = Level(LEVELS[self.level_index])
        self.player = Player(self)

        self.bind_keys()

    def bind_keys(self):
        self.screen.onkey(lambda: self.player.move(-STEP, 0), "Left")
        self.screen.onkey(lambda: self.player.move(STEP, 0), "Right")
        self.screen.onkey(lambda: self.player.move(0, STEP), "Up")
        self.screen.onkey(lambda: self.player.move(0, -STEP), "Down")

    def show_message(self, text, text_color, bg_color):
        self.screen.bgcolor(bg_color)
        self.writer.clear()
        self.writer.color(text_color)
        self.writer.write(text, font=("Arial", 28, "normal"))
        sleep(1)
        self.writer.clear()
        self.screen.bgcolor("white")

    def next_level(self):
        self.level.clear_wrong_answers()
        self.level_index += 1
        self.show_message(f"Рівень {self.level_index} пройдено!", "green", "orange")

        if self.level_index == len(LEVELS):
            self.show_message("Перемога!", "white", "green")
            self.show_message(f"Помилок: {self.errors} шт!", "white", "green")
            return

        self.level = Level(LEVELS[self.level_index])
        self.player.goto(0, 0)
