from math import hypot
from pygame import *
from random import randint

# Налаштування
size = (1000, 800)
init()
window = display.set_mode(size)
clock = time.Clock()


class Ball:
    def __init__(self, x, y, radius, color):
        self.x, self.y = x, y
        self.radius = radius
        self.color = color
        self.scale = 1.0
        self.growth_limit = 60

    def draw(self, surface, camera_x, camera_y, camera_scale):
        # Розрахунок позиції відносно гравця (камери)
        sx = int((self.x - camera_x) * camera_scale + size[0] // 2)
        sy = int((self.y - camera_y) * camera_scale + size[1] // 2)
        r = int(self.radius * camera_scale)
        draw.circle(surface, self.color, (sx, sy), max(2, r))

    def collidecircle(self, other_x, other_y, other_radius):
        distance = hypot(self.x - other_x, self.y - other_y)
        return distance < (self.radius + other_radius)


# Ініціалізація гравця
player = Ball(0, 0, 30, (0, 255, 100))

# Генерація їжі (яблук)
cells = [Ball(randint(-1000, 1000), randint(-1000, 1000), 10,
              (randint(50, 200), randint(50, 200), randint(50, 200))) for _ in range(100)]

running = True
while running:
    for e in event.get():
        if e.type == QUIT: running = False

    window.fill((40, 40, 40))

    # Логіка руху
    keys = key.get_pressed()
    speed = 15 * player.scale
    if keys[K_UP]: player.y -= speed
    if keys[K_DOWN]: player.y += speed
    if keys[K_LEFT]: player.x -= speed
    if keys[K_RIGHT]: player.x += speed

    # Оновлення масштабу
    player.scale = player.growth_limit / player.radius if player.radius > player.growth_limit else 1.0

    # Логіка поїдання
    to_remove = []
    for cell in cells:
        # Малюємо їжу
        cell.draw(window, player.x, player.y, player.scale)

        # Перевірка зіткнення
        if player.collidecircle(cell.x, cell.y, cell.radius):
            to_remove.append(cell)
            player.radius += cell.radius * 0.2

    for cell in to_remove:
        cells.remove(cell)
        # Додаємо нове яблуко замість з'їденого
        # cells.append(Ball(randint(-1000, 1000), randint(-1000, 1000), 10, (200, 200, 0)))

    # Малювання гравця
    player.draw(window, player.x, player.y, player.scale)

    display.update()
    clock.tick(60)

quit()
