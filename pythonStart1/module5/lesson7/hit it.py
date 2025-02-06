from turtle import*
from random import randint


tsize = 20
s_width = 200
s_height = 180


class Sprite(Turtle):
    def __init__(self,x,y,step=10,shape='circle',color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
        self.points = 0


    def move_up(self):
        self.goto(self.xcor(),self.ycor() + self.step)

    def move_down(self):
        self.goto(self.xcor(),self.ycor() - self.step)

    def move_left(self):
        self.goto(self.xcor() -self.step, self.ycor())

    def move_right(self):
        self.goto(self.xcor() +self.step,self.ycor())



    ##########################################
    # метод для обробки зіткнень між двома спрайтами
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist <30:
            return True
        else:
            return False

    # метод для задання координат, напрямку, переміщення
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards (x_end, y_end))#напрямок

    # метод для плавності переміщення, та визначення моменту повороту
    def make_step(self):
        self.forward(self.step)#напрямок вже є

        if self.distance(self.x_end, self.y_end) < self.step:#якщо відстань менша за півкроку
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)#міняємо напрям

############################################


player = Sprite(0, -100,10,'circle','orange')
enemy1 = Sprite(-s_width,0,15,'square','red')
enemy2 = Sprite(s_width,70,15,'square','red')
goal = Sprite(0,120,20,'triangle','green')


########################
# ставимо в правильне місце червоні спрайти
enemy1.set_move(-s_width,0, s_width,0)
enemy2.set_move(s_width,70, -s_width,70)
goal.set_move(-s_width, 120, s_width, 0)
# встановлюємо лічильник рахунку
total_score = 0
########################



scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up,'Up')
scr.onkey(player.move_left,'Left')
scr.onkey(player.move_right,'Right')
scr.onkey(player.move_down,'Down')




#########################

while total_score <3:
    # запускаємо червоні спрайти
    enemy1.make_step()
    enemy2.make_step()
    goal.make_step()
    if player.is_collide(goal):
        total_score += 1
        player.goto(0, -100)
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        goal.hideturtle()
        break


if total_score == 3:
    enemy1.hideturtle()
    enemy2.hideturtle()

