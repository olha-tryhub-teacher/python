from math import hypot
from pygame import *
from random import randint
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


def receive_data():
    global all_players, lose
    while True:
        try:
            data = sock.recv(4096).decode()
            if "LOSE" in data:
                lose = True
            elif data:
                # 1. Створюємо тимчасовий словник
                temp_players = {}

                for p in data.split("|"):
                    if "," in p:
                        parts = p.split(",")
                        if len(parts) >= 4:
                            pid = int(parts[0])
                            if pid != my_id:
                                temp_players[pid] = [int(parts[1]), int(parts[2]), int(parts[3])]

                # 2. Повністю замінюємо старі дані новими.
                # Тих, кого з'їли, тут уже не буде!
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
        # Масштабування
        self.scale = self.growth_limit / self.radius if self.radius > self.growth_limit else 1.0

        keys = key.get_pressed()
        speed = 15 * self.scale
        if keys[K_UP]: self.y -= speed
        if keys[K_DOWN]: self.y += speed
        if keys[K_LEFT]: self.x -= speed
        if keys[K_RIGHT]: self.x += speed

        # Логіка поїдання (спрощено)
        for cell in cells[:]:
            if self.collidecircle(cell):
                self.radius += cell.radius * 0.2
                cells.remove(cell)

    def draw(self, surface, camera_x, camera_y, camera_scale):
        sx = int((self.x - camera_x) * camera_scale + size[0] // 2)
        sy = int((self.y - camera_y) * camera_scale + size[1] // 2)
        r = int(self.radius * camera_scale)
        draw.circle(surface, self.color, (sx, sy), max(2, r))

    def collidecircle(self, ball2):
        distance = hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)

# Ініціалізація
ball = Ball(my_x, my_y, my_r, (0, 255, 100), speed=15)
cells = [Ball(randint(-2000, 2000), randint(-2000, 2000), 10, "#E8B888") for _ in range(300)]
f = font.Font(None, 50)
running, lose = True, False

while running:
    for e in event.get():
        if e.type == QUIT: running = False

    window.fill((40, 40, 40))

    if not lose:
        ball.update_player(cells)
        # Відправка своїх координат на сервер
        sock.send(f"{my_id},{int(ball.x)},{int(ball.y)},{int(ball.radius)},Player".encode())

    # Малювання яблук
    for cell in cells:
        cell.draw(window, ball.x, ball.y, ball.scale)

    # Малювання ворогів
    for pid, data in all_players.items():
        # Малюємо ворога як червоне коло
        ox, oy, orad = data
        sx = int((ox - ball.x) * ball.scale + size[0] // 2)
        sy = int((oy - ball.y) * ball.scale + size[1] // 2)
        draw.circle(window, (255, 50, 50), (sx, sy), max(4, int(orad * ball.scale)))

    if not lose:
        ball.draw(window, ball.x, ball.y, 1.0 if ball.radius < 60 else ball.scale)
    else:
        window.blit(f.render("U lose!", 1, (244, 0, 0)), (400, 500))

    display.update()
    clock.tick(60)

quit()
