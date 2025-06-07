from pygame import *
from math import hypot


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

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

rect = Rect(100, 100, 50, 50)
ball = Ball(300, 300, 25, (255, 100, 255))

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    keys = key.get_pressed()
    if keys[K_w]:
        rect.y -= 3
    if keys[K_s]:
        rect.y += 3
    if keys[K_a]:
        rect.x -= 3
    if keys[K_d]:
        rect.x += 3

    if keys[K_UP]:
        ball.y -= 3
    if keys[K_DOWN]:
        ball.y += 3
    if keys[K_LEFT]:
        ball.x -= 3
    if keys[K_RIGHT]:
        ball.x += 3

    # window.blit(bg, (0, 0))
    draw.rect(window, (100, 255, 255), rect)
    ball.reset()

    display.update()
    clock.tick(60)



