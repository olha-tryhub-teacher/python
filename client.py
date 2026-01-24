from math import hypot
from pygame import *
from random import randint  # ⬅️
import socket
import pickle  # ⬅️
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ⬅️
client.connect(("127.0.0.1", 5555))  # ⬅️

other_players_balls = {}  # ⬅️
my_id = None  # ⬅️

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

    def draw(self, center_x, center_y, scale):
        sx = int((self.x - center_x) * scale + WINDOW_SIZE[0] // 2)
        sy = int((self.y - center_y) * scale + WINDOW_SIZE[1] // 2)
        draw.circle(window, self.color, (sx, sy), int(self.radius * scale))

    def collidecircle(self, other):
        distance = hypot(self.x - other.x, self.y - other.y)
        return distance <= self.radius + other.radius

    def draw_center(self, scale):
        draw.circle(
            window,
            self.color,
            (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2),
            int(self.radius * scale)
        )

# ⬇️⬇️⬇️
def receive_data():  # ⬅️
    global my_id, other_players_balls
    while True:
        try:
            data = client.recv(4096)
            msg = pickle.loads(data)

            if msg["type"] == "id":
                my_id = msg["id"]
                print("My ID:", my_id)

            elif msg["type"] == "state":
                players = msg["players"]

                # оновлюємо / створюємо кульки ворогів
                for pid, (x, y, r) in players.items():
                    if my_id is not None and pid == my_id:
                        continue

                    if pid not in other_players_balls:
                        other_players_balls[pid] = Ball(x, y, r, (255, 0, 0))
                    else:
                        b = other_players_balls[pid]
                        b.x = x
                        b.y = y
                        b.radius = r

                # видаляємо гравців, які вийшли
                for pid in list(other_players_balls.keys()):
                    if pid not in players:
                        del other_players_balls[pid]

        except Exception as e:
            print("Receive error:", e)
            break



# Налаштування
WINDOW_SIZE = 700, 500
PLAYER_SPEED = 10

# Pygame
init()
window = display.set_mode(WINDOW_SIZE)
clock = time.Clock()

# Гравець (був ball)
player = Ball(0, 0, 20, (0, 255, 0), PLAYER_SPEED)

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

threading.Thread(target=receive_data, daemon=True).start()   # ⬅️

# Основний цикл
running = True
while running:

    for e in event.get():
        if e.type == QUIT:
            running = False

    window.fill((255, 255, 255))

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

    client.sendall(pickle.dumps((player.x, player.y, player.radius)))   # ⬅️
    for ball in other_players_balls.values():  # ⬅️
        ball.draw(player.x, player.y, scale)  # ⬅️

    display.update()
    clock.tick(60)

quit()

