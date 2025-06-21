from math import hypot
from pygame import *
from random import randint

from socket import socket, AF_INET, SOCK_STREAM  # 🆕 Додано імпорт для роботи з мережею (TCP сокети)
from threading import Thread  # 🆕 Імпорт для створення окремого потоку

# 🆕 Створення сокета і підключення до сервера (локально на порт 8080)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 8080))
# 🆕 Отримуємо стартові дані від сервера — список: [id, x, y, r]
my_data = list(map(int, sock.recv(64).decode().strip().split(',')))
my_id = my_data[0]
my_player = my_data[1:]

sock.setblocking(False)  # 🆕 Робимо сокет неблокуючим (щоб не зависав при recv)

# === Налаштування гри ===
# my_player = [0, 0, 20]  # [x, y, радіус] - головний гравець (зелена кулька)
my_player_speed = 10  # швидкість руху гравця
window_size = 700, 500  # розміри вікна

# Ініціалізація Pygame
init()
window = display.set_mode(window_size)
clock = time.Clock()
f = font.Font(None, 50)
all_players = []
running = True
lose = False


# 🆕 Функція, яка постійно слухає сервер у фоновому потоці
def receive_data():
    global all_players, running, lose
    while running:
        try:
            data = sock.recv(4096).decode().strip()
            if data == "LOSE":  # Якщо прийшло повідомлення поразки
                lose = True
            elif data:
                parts = data.strip('|').split('|')  # Розділяємо всі гравці
                all_players = [list(map(int, p.split(',')))
                               for p in parts if len(p.split(',')) == 4]
        except:
            pass


Thread(target=receive_data, daemon=True).start()  # 🆕 Запускаємо прийом даних у окремому потоці


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
other_cells = [Cell(randint(-2000, 2000),  # випадкова позиція x
                    randint(-2000, 2000),  # випадкова позиція y
                    10,  # радіус 10
                    (randint(0, 255),  # випадковий колір (R)
                     randint(0, 255),  # G
                     randint(0, 255)))  # B
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

    # 🆕 Малюємо всіх інших гравців червоними кружечками
    for p in all_players:
        if p[0] == my_id: continue  # Пропускаємо себе
        sx = int((p[1] - my_player[0]) * scale + 500)
        sy = int((p[2] - my_player[1]) * scale + 500)
        draw.circle(window, (255, 0, 0), (sx, sy), int(p[3] * scale))


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

    # 🆕 Якщо гравець програв — виводимо повідомлення
    if lose:
        t = f.render('U lose!', 1, (244, 0, 0))
        window.blit(t, (400, 500))

    # === Керування гравцем (рух W, A, S, D) ===
    # 🆕 Якщо ще не програв — можна керувати гравцем
    if not lose:
        keys = key.get_pressed()
        if keys[K_w]: my_player[1] -= my_player_speed
        if keys[K_s]: my_player[1] += my_player_speed
        if keys[K_a]: my_player[0] -= my_player_speed
        if keys[K_d]: my_player[0] += my_player_speed

        # 🆕 Надсилаємо оновлену позицію на сервер
        try:
            msg = f"{my_id},{my_player[0]},{my_player[1]},{my_player[2]}"
            sock.send(msg.encode())
        except:
            pass

    # Оновлення екрану
    display.update()
    clock.tick(60)  # 60 кадрів на секунду

# === Завершення гри ===
quit()
