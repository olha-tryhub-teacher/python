from turtle import *
from time import sleep

screen = getscreen()
screen.bgcolor("white")
# screen.tracer(0)
hideturtle()
pu()
goto(-200, 150)


def info(text, col, bg):
    """Для відображення інформації"""
    screen.bgcolor(bg)
    color(col)
    write(text, font=("Arial", 28, "normal"))
    # update()
    sleep(1)
    clear()
    screen.bgcolor("white")
    # update()


class Player(Turtle):
    errors = 0

    def __init__(self, x, y, game):
        super().__init__(shape="square")
        self.color("green")
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.game = game

        screen.onkey(self.__move_left, "Left")
        screen.onkey(self.__move_right, "Right")
        screen.onkey(self.__move_up, "Up")
        screen.onkey(self.__move_down, "Down")

    def __move_left(self):
        self.setheading(180)
        self.forward(10)
        self.check_collision()

    def __move_right(self):
        self.setheading(0)
        self.forward(10)
        self.check_collision()

    def __move_up(self):
        self.setheading(90)
        self.forward(10)
        self.check_collision()

    def __move_down(self):
        self.setheading(-90)
        self.forward(10)
        self.check_collision()

    def check_collision(self):
        """Перевірка зіткнення з роботами поточного рівня"""
        end_level = False
        for robot in self.game.level.robots:
            if self.distance(robot.pos()) < 20 and robot.isvisible():
                robot.clear()
                robot.hideturtle()
                if robot.is_right:
                    end_level = True
                    robot.pendown()
                    robot.move()
                    break
                else:
                    Player.errors += 1

        if end_level:
            for robot in self.game.level.robots:
                if not robot.is_right:
                    robot.clear()
                    robot.hideturtle()
            self.game.next_level()

        # update()


class Robot(Turtle):
    """Клас робота який малює лінію, якщо відповідь правильна"""

    def __init__(self, x1, y1, x2, y2, color_val, text, is_right=False):
        super().__init__("classic")
        self.hideturtle()
        self.is_right = is_right
        self.speed(0)
        self.color(color_val)
        self.penup()
        self.goto(x1, y1)
        self.showturtle()
        self.write(text, font=("Arial", 16, "normal"))
        # для майбутнього переміщення
        self.__command_x = x2
        self.__command_y = y2

    def move(self):
        if self.is_right:
            self.goto(self.__command_x, self.__command_y)


class Level:
    """логіка рівня, вівень складається з роботів, перевіряється зіткнення робота з гравцем"""

    def __init__(self):
        self.colorsList = ("red", "blue", "orange", "green")
        self.robots = []
        # Прапорець закінчення рівня
        self.end_level = False

    def add_robot(self, x1, y1, x2, y2, text, is_right):
        # Використовуємо колір із списку для кожного робота
        color_val = self.colorsList[len(self.robots)]
        r = Robot(x1, y1, x2, y2, color_val, text, is_right)
        self.robots.append(r)


class Game:
    """Клас гри"""

    def __init__(self):
        self.currentLevel = 0
        self.create_level1()
        self.player = Player(0, 0, self)

    def create_level1(self):
        level = Level()
        level.add_robot(-80, -120, -200, 0, "Сідней", True)
        level.add_robot(-80, 120, 0, 0, "Берлін", False)
        level.add_robot(80, 120, 0, 0, "Рим", False)
        level.add_robot(80, -120, 0, 0, "Київ", False)
        self.level = level

    def create_level2(self):
        level = Level()
        level.add_robot(-80, 120, 0, 0, "Атлантичний", False)
        level.add_robot(200, 0, 120, -120, "Китайський", True)
        level.add_robot(80, 120, 0, 0, "Індійський", False)
        level.add_robot(80, -120, 0, 0, "Тихий", False)
        self.level = level

    def create_level3(self):
        level = Level()
        level.add_robot(-200, 120, 0, 0, "Python", False)
        level.add_robot(100, 120, 0, 0, "C++", False)
        level.add_robot(0, 0, 0, 200, "Mouse", True)
        level.add_robot(0, -120, 0, 0, "JavaAcript", False)
        self.level = level

    def create_level4(self):
        level = Level()
        level.add_robot(-80, 120, 0, 0, "Cat", False)
        level.add_robot(80, 120, 0, 0, "Dog", False)
        level.add_robot(0, -120, 0, 0, "Mouse", False)
        level.add_robot(0, 200, 160, 40, "Shark", True)
        self.level = level

    def create_level5(self):
        level = Level()
        level.add_robot(120, -120, -80, -120, "Head", True)
        level.add_robot(-120, -120, 0, 0, "CPU", False)
        level.add_robot(0, 0, 0, 0, "SSD", False)
        level.add_robot(150, 0, 0, 0, "RAM", False)
        self.level = level

    def create_level6(self):
        level = Level()
        level.add_robot(-80, 120, 0, 0, "Red", False)
        level.add_robot(-120, 40, 0, 200, "Brawl", True)
        level.add_robot(80, 120, 0, 0, "Green", False)
        level.add_robot(100, 0, 0, 0, "Blue", False)
        self.level = level

    def create_level7(self):
        level = Level()
        level.add_robot(-80, 120, 0, 0, "Train", False)
        level.add_robot(80, 120, 0, 0, "Car", False)
        level.add_robot(-200, 0, 200, 0, "Seat", True)
        level.add_robot(120, 0, 0, 0, "Rocket", False)
        self.level = level

    def create_level8(self):
        level = Level()
        level.add_robot(-80, 120, 0, 0, "One", False)
        level.add_robot(80, 120, 0, 0, "Two", False)
        level.add_robot(80, -120, 0, 0, "Three", False)
        level.add_robot(160, 40, -120, 40, "Minus", True)
        self.level = level

    def next_level(self):
        self.currentLevel += 1
        info(f"Рівень {self.currentLevel} пройдено!", "green", "orange")
        if self.currentLevel == 1:
            self.create_level2()
        elif self.currentLevel == 2:
            self.create_level3()
        elif self.currentLevel == 3:
            self.create_level4()
        elif self.currentLevel == 4:
            self.create_level5()
        elif self.currentLevel == 5:
            self.create_level6()
        elif self.currentLevel == 6:
            self.create_level7()
        elif self.currentLevel == 7:
            self.create_level8()
        if self.currentLevel >= 8:
            info("Перемога!", "white", "green")
            info(f"Помилок: {Player.errors} шт!", "white", "green")


game = Game()
screen.listen()
done()
