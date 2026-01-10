from math import hypot
from pygame import *
from random import randint  # ⬅️

# Клас кульки
class Ball:
    def __init__(self, x, y, radius, color, speed=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

    def move(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.y -= self.speed
        if keys[K_s]:
            self.y += self.speed
        if keys[K_a]:
            self.x -= self.speed
        if keys[K_d]:
            self.x += self.speed

    # ⬇️⬇️⬇️ 🔃🔃🔃
    def draw(self, center_x, center_y, scale):
        sx = int((self.x - center_x) * scale + WINDOW_SIZE[0] // 2)
        sy = int((self.y - center_y) * scale + WINDOW_SIZE[1] // 2)
        draw.circle(window, self.color, (sx, sy), int(self.radius * scale))

    def collidecircle(self, other):
        distance = hypot(self.x - other.x, self.y - other.y)
        return distance <= self.radius + other.radius

    # ⬇️⬇️⬇️
    def draw_center(self, scale):
        draw.circle(
            window,
            self.color,
            (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2),
            int(self.radius * scale)
        )


# Налаштування
WINDOW_SIZE = 700, 500 # ⬅️🔃
PLAYER_SPEED = 10 # ⬅️

# Pygame
init()
window = display.set_mode(WINDOW_SIZE)
clock = time.Clock()

# Гравець (був ball)
player = Ball(0, 0, 20, (0, 255, 0), PLAYER_SPEED)# ⬅️🔃

# ⬇️⬇️⬇️
# Інші кульки
balls = [
    Ball(
        randint(-2000, 2000),
        randint(-2000, 2000),
        10,
        (randint(0, 255), randint(0, 255), randint(0, 255))
    )
    for _ in range(300)
]

# Основний цикл
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    window.fill((0, 0, 0))

    # Масштаб (чим більший гравець — тим менший зум)
    scale = max(0.3, min(50 / player.radius, 1.5))

    # Рух гравця
    player.move()

    # Малювання гравця
    player.draw_center(scale)

    # Кульки
    to_remove = []
    for ball in balls:
        if player.collidecircle(ball):
            to_remove.append(ball)
            player.radius += int(ball.radius * 0.2)
        else:
            ball.draw(player.x, player.y, scale)

    for ball in to_remove:
        balls.remove(ball)

    display.update()
    clock.tick(60)

quit()
