from math import hypot
from pygame import *
from random import randint

# === Налаштування гри ===
my_player = [0, 0, 20]  # [x, y, радіус] - головний гравець (зелена кулька)
my_player_speed = 10  # швидкість руху гравця
window_size = 700, 500  # розміри вікна

# Ініціалізація Pygame
init()
window = display.set_mode(window_size)
clock = time.Clock()
f = font.Font(None, 50)  # шрифт (можна використати для написів)
all_players = []  # не використовується, можна прибрати
lose = False  # змінна для поразки (не використовується зараз)


# === Клас для інших клітин (маленькі кульки) ===
class Cell:
    def __init__(self, x, y, r, c):
        self.x = x  # координата X
        self.y = y  # координата Y
        self.radius = r  # радіус кульки
        self.color = c  # колір кульки (RGB)

    def check_collision(self, player_x, player_y, player_r):
        # Перевірка на зіткнення з гравцем (відстань менша за суму радіусів)
        dx = self.x - player_x
        dy = self.y - player_y
        return hypot(dx, dy) <= self.radius + player_r


# === Створення випадкових кульок на мапі ===
other_cells = [Cell(randint(-2000, 2000), randint(-2000, 2000),  # випадкова позиція y
                    10,  # радіус 10
                    (randint(0, 255), randint(0, 255),  randint(0, 255)))  # B
               for _ in range(300)]  # створити 300 кульок

# === Основний ігровий цикл ===
running = True
while running:
    # Обробка подій (наприклад, вихід з гри)
    for e in event.get():
        if e.type == QUIT:
            running = False

    # Очищення екрана
    window.fill((255, 255, 255))  # білий фон

    # Масштаб залежно від розміру гравця: чим більший — тим менший масштаб
    scale = max(0.3, min(50 / my_player[2], 1.5))

    # Малювання гравця в центрі екрана
    draw.circle(window, (0, 255, 0),
                (window_size[0] // 2, window_size[1] // 2),
                int(my_player[2] * scale))

    # === Малювання та обробка інших клітин ===
    to_remove = []  # список кульок, які потрібно прибрати
    for c in other_cells:
        if c.check_collision(my_player[0], my_player[1], my_player[2]):
            # Якщо зіткнення — додати до списку на видалення і збільшити гравця
            to_remove.append(c)
            my_player[2] += int(c.radius * 0.2)  # гравець росте після поглинання
        else:
            # Якщо не зіткнення — малюємо кульку на екрані, враховуючи масштаб і центр
            sx = int((c.x - my_player[0]) * scale + window_size[0] // 2)
            sy = int((c.y - my_player[1]) * scale + window_size[1] // 2)
            draw.circle(window, c.color, (sx, sy), int(c.radius * scale))

    # Видаляємо поглинуті кульки
    for c in to_remove:
        other_cells.remove(c)

    # === Керування гравцем (рух W, A, S, D) ===
    keys = key.get_pressed()
    if keys[K_w]: my_player[1] -= my_player_speed
    if keys[K_s]: my_player[1] += my_player_speed
    if keys[K_a]: my_player[0] -= my_player_speed
    if keys[K_d]: my_player[0] += my_player_speed

    # Оновлення екрану
    display.update()
    clock.tick(60)  # 60 кадрів на секунду

# === Завершення гри ===
quit()
