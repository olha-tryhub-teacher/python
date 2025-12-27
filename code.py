from pygame import *
from math import hypot


class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def move(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            ball.y -= self.speed
        if keys[K_DOWN]:
            ball.y += self.speed
        if keys[K_LEFT]:
            ball.x -= self.speed
        if keys[K_RIGHT]:
            ball.x += self.speed

    def reset(self):
        draw.circle(window, self.color, (self.x, self.y), self.radius)

    def collidecircle(self, ball2):
        distance = hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)


init()

size = 500, 500

window = display.set_mode(size)
display.set_caption("ВАША НАЗВА")
clock = time.Clock()

# bg = image.load("img.png")
# bg = transform.scale(bg, size)

ball = Ball(300, 300, 25, (255, 100, 255), 5)

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    screen.fill((255, 255, 255))
    # window.blit(bg, (0, 0))
    ball.move()
    ball.reset()

    display.update()
    clock.tick(60)



