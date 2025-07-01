from math import hypot
from socket import socket, AF_INET, SOCK_STREAM
from pygame import *
from threading import Thread
from random import randint
from launcher import ConnectWindow

size = (1000, 800)
bg = image.load("images/grass.png")
bg = transform.scale(bg, size)
# 
# player = image.load("images/cat.png")
# apple = image.load("images/apple.png")

win = ConnectWindow()
win.mainloop()

name = win.name
port = win.port
host = win.host
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host, port))
resv_my_data = sock.recv(64).decode().strip().strip("|").split(',')
my_data = list(map(int, resv_my_data))
my_id = my_data[0]
my_player = my_data[1:]
sock.setblocking(False)

init()
window = display.set_mode(size)
clock = time.Clock()
f = font.Font(None, 50)
all_players = []
running = True
lose = False


def receive_data():
    global all_players, running, lose
    while running:
        try:
            data = sock.recv(4096).decode().strip()
            if data == "LOSE":
                lose = True
            elif data:
                parts = data.strip('|').split('|')

                all_players = [list(map(int, p.split(',')[:4])) + [p.split(',')[4]] for p in parts if
                               len(p.split(',')) == 5]
        except:
            pass


Thread(target=receive_data, daemon=True).start()


class Cell:
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.radius = r
        self.color = c

    def check_collision(self, player_x, player_y, player_r):
        dx = self.x - player_x
        dy = self.y - player_y
        return hypot(dx, dy) <= self.radius + player_r


cells = [Cell(randint(-2000, 2000), randint(-2000, 2000), 10,
              (randint(0, 255), randint(0, 255), randint(0, 255))
              )
         for _ in range(300)]
name_font = font.Font(None, 20)
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    # window.fill((255, 255, 255))
    window.blit(bg, (0, 0))
    scale = max(0.3, min(50 / my_player[2], 1.5))

    for p in all_players:
        if p[0] == my_id: continue
        sx = int((p[1] - my_player[0]) * scale + size[0] // 2)
        sy = int((p[2] - my_player[1]) * scale + size[1] // 2)
        draw.circle(window, (255, 0, 0), (sx, sy), int(p[3] * scale))
        name_text = name_font.render(f'{p[4]}', 1, (0, 0, 0))
        window.blit(name_text, (sx, sy))

    draw.circle(window, (0, 255, 0), (size[0]//2, size[1]//2), int(my_player[2] * scale))
    # window.blit(
    #     transform.scale(
    #         player,
    #         (my_player[2] * scale * 2, my_player[2] * scale * 2)
    #     ),
    #     (size[0]//2 - my_player[2] * scale,
    #      size[1]//2 - my_player[2] * scale))

    to_remove = []
    for cell in cells:
        if cell.check_collision(my_player[0], my_player[1], my_player[2]):
            to_remove.append(cell)
            my_player[2] += int(cell.radius * 0.2)
        else:
            sx = int((cell.x - my_player[0]) * scale + size[0] // 2)
            sy = int((cell.y - my_player[1]) * scale + size[1] // 2)
            draw.circle(window, cell.color, (sx, sy), int(cell.radius * scale))
            # window.blit(transform.scale(apple, (cell.radius * 2, cell.radius * 2)), (sx, sy))

    for cell in to_remove:
        cells.remove(cell)

    if lose:
        t = f.render('U lose!', 1, (244, 0, 0))
        window.blit(t, (400, 500))

    display.update()
    clock.tick(60)

    if not lose:
        keys = key.get_pressed()
        if keys[K_w]: my_player[1] -= 15
        if keys[K_s]: my_player[1] += 15
        if keys[K_a]: my_player[0] -= 15
        if keys[K_d]: my_player[0] += 15

        try:
            msg = f"{my_id},{my_player[0]},{my_player[1]},{my_player[2]},{name}"
            sock.send(msg.encode())
        except:
            pass

quit()
