import os
from math import hypot
from pygame import *
from random import randint, choice  # ДОДАНО: choice для вибору випадкового елемента
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

# Налаштування мережі
HOST = "127.0.0.1"
PORT = 5000
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORT))

# Отримуємо свої дані при старті
resv_data = sock.recv(64).decode().split(",")
my_id, my_x, my_y, my_r = map(int, resv_data)

# Налаштування вікна
size = (1000, 800)
init()
window = display.set_mode(size)
clock = time.Clock()

all_players = {}  # Словник {id: [x, y, r]}
enemy_images = {}  # НОВЕ: Словник для збереження закріплених картинок за ворогами {id: image}

# ==========================================
# 1. ЗАВАНТАЖЕННЯ УСІХ КАРТИНОК
# ==========================================
player_images = []
folder_path = "images/players"

# Перевіряємо, чи існує папка, щоб уникнути помилок
if os.path.exists(folder_path):
    for filename in os.listdir(folder_path):
        # Відбираємо тільки файли зображень
        if filename.endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder_path, filename)
            player_images.append(image.load(img_path))

# Якщо папка порожня або її немає, створюємо запасну картинку
if not player_images:
    backup_img = Surface((50, 50))
    backup_img.fill((0, 255, 0))
    player_images.append(backup_img)
# ==========================================

bg_img = image.load("images/img.png")

# 2. НАДАЄМО СОБІ ВИПАДКОВУ КАРТИНКУ
my_player_img = choice(player_images)


def receive_data():
    global all_players, lose
    while True:
        try:
            data = sock.recv(4096).decode()
            if "LOSE" in data:
                lose = True
            elif data:
                temp_players = {}
                for p in data.split("|"):
                    if "," in p:
                        parts = p.split(",")
                        if len(parts) >= 4:
                            pid = int(parts[0])
                            if pid != my_id:
                                temp_players[pid] = [int(parts[1]), int(parts[2]), int(parts[3])]

                all_players = temp_players
        except:
            break


Thread(target=receive_data, daemon=True).start()


class Ball:
    def __init__(self, x, y, radius, color, speed=0):
        self.x, self.y = x, y
        self.radius = radius
        self.color = color
        self.base_speed = speed
        self.scale = 1.0
        self.growth_limit = 60

    def update_player(self, cells):
        self.scale = self.growth_limit / self.radius if self.radius > self.growth_limit else 1.0
        keys = key.get_pressed()
        speed = 15 * self.scale
        if keys[K_UP]: self.y -= speed
        if keys[K_DOWN]: self.y += speed
        if keys[K_LEFT]: self.x -= speed
        if keys[K_RIGHT]: self.x += speed

        for cell in cells[:]:
            if self.collidecircle(cell):
                self.radius += cell.radius * 0.2
                cells.remove(cell)

    def draw(self, surface, camera_x, camera_y, camera_scale, img=None):
        sx = int((self.x - camera_x) * camera_scale + size[0] // 2)
        sy = int((self.y - camera_y) * camera_scale + size[1] // 2)
        r = int(self.radius * camera_scale)

        if img:
            scaled_img = transform.scale(img, (r * 2, r * 2))
            surface.blit(scaled_img, (sx - r, sy - r))
        else:
            draw.circle(surface, self.color, (sx, sy), max(2, r))

    def collidecircle(self, ball2):
        distance = hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)


# Ініціалізація
ball = Ball(my_x, my_y, my_r, (0, 255, 100), speed=15)
cells = [Ball(randint(-2000, 2000), randint(-2000, 2000), 10, "#E8B888") for _ in range(300)]
f = font.Font(None, 50)
running, lose = True, False

WORLD_SIZE = 4000

while running:
    for e in event.get():
        if e.type == QUIT: running = False

    window.fill((40, 40, 40))

    bg_scaled_size = int(WORLD_SIZE * ball.scale)
    scaled_bg = transform.scale(bg_img, (bg_scaled_size, bg_scaled_size))

    base_bg_x = int((-2000 - ball.x) * ball.scale + size[0] // 2)
    base_bg_y = int((-2000 - ball.y) * ball.scale + size[1] // 2)

    start_x = (base_bg_x % bg_scaled_size) - bg_scaled_size
    start_y = (base_bg_y % bg_scaled_size) - bg_scaled_size

    for x in range(start_x, size[0], bg_scaled_size):
        for y in range(start_y, size[1], bg_scaled_size):
            window.blit(scaled_bg, (x, y))

    if not lose:
        ball.update_player(cells)
        sock.send(f"{my_id},{int(ball.x)},{int(ball.y)},{int(ball.radius)},Player".encode())

    # Малювання яблук
    for cell in cells:
        cell.draw(window, ball.x, ball.y, ball.scale)

    # Малювання ворогів
    for pid, data in all_players.items():
        ox, oy, orad = data

        # НОВЕ: Якщо ми бачимо цього гравця вперше, обираємо йому випадкову картинку
        if pid not in enemy_images:
            enemy_images[pid] = choice(player_images)

        sx = int((ox - ball.x) * ball.scale + size[0] // 2)
        sy = int((oy - ball.y) * ball.scale + size[1] // 2)
        r = max(4, int(orad * ball.scale))

        # Беремо закріплену за цим id картинку
        scaled_enemy = transform.scale(enemy_images[pid], (r * 2, r * 2))
        window.blit(scaled_enemy, (sx - r, sy - r))

    if not lose:
        # НОВЕ: Передаємо обрану на старті my_player_img
        ball.draw(window, ball.x, ball.y, 1.0 if ball.radius < 60 else ball.scale, img=my_player_img)
    else:
        window.blit(f.render("U lose!", 1, (244, 0, 0)), (400, 500))

    display.update()
    clock.tick(60)

quit()
